#!/usr/bin/env python3
"""
Stacks DeGrants Phase III - Social Score Analyzer
Leverages LunarCrush API to evaluate grant applicants' social presence
"""

import requests
import pandas as pd
import json
from typing import Dict, List, Optional, Tuple
from dotenv import load_dotenv
import os
from datetime import datetime

class StacksDeGrantsAnalyzer:
    """
    Social Score Analyzer for Stacks DeGrants Phase III Applications
    
    This class provides comprehensive social analytics for grant evaluation,
    helping identify applicants with significant social presence and influence.
    """
    
    def __init__(self):
        """Initialize the analyzer with LunarCrush API credentials"""
        load_dotenv()
        self.api_key = os.getenv('LUNARCRUSH_API_KEY')
        if not self.api_key:
            raise ValueError("LUNARCRUSH_API_KEY not found in environment variables")
        
        self.base_url = "https://lunarcrush.com/api4"
        self.headers = {"Authorization": f"Bearer {self.api_key}"}
        
        # Social score weights for grant evaluation
        self.weights = {
            'galaxy_score': 0.30,      # Overall influence (30%)
            'interactions': 0.25,      # Engagement volume (25%)
            'sentiment': 0.20,         # Community perception (20%)
            'platforms': 0.15,        # Multi-platform presence (15%)
            'consistency': 0.10         # Long-term activity (10%)
        }
        
        # Flagging thresholds
        self.thresholds = {
            'high_social_score': 70,
            'high_engagement': 1000000,  # 1M interactions
            'positive_sentiment': 80,
            'multi_platform': 3
        }
    
    def search_creator(self, handle: str) -> Optional[Dict]:
        """
        Search for a creator by social handle
        
        Args:
            handle: Social media handle (e.g., '@alice_crypto')
            
        Returns:
            Creator data if found, None otherwise
        """
        try:
            # Clean handle (remove @ if present)
            clean_handle = handle.lstrip('@')
            
            # Search creators endpoint
            url = f"{self.base_url}/public/creators/search/v1"
            params = {'q': clean_handle, 'limit': 5}
            
            response = requests.get(url, headers=self.headers, params=params, timeout=10)
            
            if response.status_code == 200:
                data = response.json()
                creators = data.get('data', [])
                
                # Find best match (exact or partial)
                for creator in creators:
                    if (clean_handle.lower() in creator.get('name', '').lower() or
                        clean_handle.lower() in creator.get('username', '').lower()):
                        return creator
                
                # Return first result if no exact match
                return creators[0] if creators else None
            
            return None
            
        except Exception as e:
            print(f"Error searching creator {handle}: {e}")
            return None
    
    def analyze_grant_applicant(self, applicant_data: Dict) -> Dict:
        """
        Analyze a grant applicant's social presence
        
        Args:
            applicant_data: Dictionary containing applicant information
                - 'id': Unique applicant identifier
                - 'name': Applicant name
                - 'social_handles': List of social media handles
                - 'project_description': Optional project description
                
        Returns:
            Comprehensive social analysis results
        """
        social_handles = applicant_data.get('social_handles', [])
        
        social_profile = {
            'applicant_id': applicant_data.get('id'),
            'applicant_name': applicant_data.get('name'),
            'total_galaxy_score': 0,
            'total_interactions': 0,
            'total_contributors': 0,
            'average_sentiment': 0,
            'platforms_analyzed': [],
            'platform_details': [],
            'social_score': 0,
            'flag_status': False,
            'flag_reasons': [],
            'analysis_timestamp': datetime.now().isoformat()
        }
        
        if not social_handles:
            social_profile['flag_reasons'].append("No social handles provided")
            return social_profile
        
        # Analyze each social handle
        valid_platforms = 0
        total_sentiment = 0
        
        for handle in social_handles:
            creator_data = self.search_creator(handle)
            
            if creator_data:
                valid_platforms += 1
                platform_info = {
                    'handle': handle,
                    'galaxy_score': creator_data.get('galaxy_score', 0),
                    'interactions_24h': creator_data.get('interactions_24h', 0),
                    'contributors': creator_data.get('num_contributors', 0),
                    'sentiment': creator_data.get('sentiment', 0),
                    'posts_24h': creator_data.get('num_posts_24h', 0),
                    'followers': creator_data.get('followers', 0)
                }
                
                social_profile['platforms_analyzed'].append(handle)
                social_profile['platform_details'].append(platform_info)
                
                # Aggregate metrics
                social_profile['total_galaxy_score'] += platform_info['galaxy_score']
                social_profile['total_interactions'] += platform_info['interactions_24h']
                social_profile['total_contributors'] += platform_info['contributors']
                total_sentiment += platform_info['sentiment']
        
        # Calculate averages
        if valid_platforms > 0:
            social_profile['average_galaxy_score'] = social_profile['total_galaxy_score'] / valid_platforms
            social_profile['average_sentiment'] = total_sentiment / valid_platforms
            social_profile['average_interactions'] = social_profile['total_interactions'] / valid_platforms
        
        # Calculate final social score
        social_profile['social_score'] = self.calculate_social_score(social_profile)
        
        # Determine flagging status
        social_profile['flag_status'], social_profile['flag_reasons'] = self.evaluate_flagging(social_profile)
        
        return social_profile
    
    def calculate_social_score(self, profile: Dict) -> float:
        """
        Calculate weighted social score for grant evaluation
        
        Args:
            profile: Social profile data
            
        Returns:
            Social score (0-100)
        """
        if not profile['platforms_analyzed']:
            return 0.0
        
        # Normalize scores to 0-100 scale
        galaxy_norm = min(profile.get('average_galaxy_score', 0), 100)
        interactions_norm = min(profile['total_interactions'] / 1000000, 100)  # Normalize to millions
        sentiment_norm = max(0, min(profile.get('average_sentiment', 0), 100))
        platforms_norm = min(len(profile['platforms_analyzed']) * 25, 100)  # 4 platforms = 100
        
        # Calculate weighted score
        social_score = (
            galaxy_norm * self.weights['galaxy_score'] +
            interactions_norm * self.weights['interactions'] +
            sentiment_norm * self.weights['sentiment'] +
            platforms_norm * self.weights['platforms']
        )
        
        return round(social_score, 2)
    
    def evaluate_flagging(self, profile: Dict) -> Tuple[bool, List[str]]:
        """
        Evaluate if applicant should be flagged for special consideration
        
        Args:
            profile: Social profile data
            
        Returns:
            Tuple of (should_flag, list_of_reasons)
        """
        flag_reasons = []
        should_flag = False
        
        # Check flagging criteria
        if profile['social_score'] >= self.thresholds['high_social_score']:
            flag_reasons.append(f"High social score ({profile['social_score']}/100)")
            should_flag = True
        
        if profile['total_interactions'] >= self.thresholds['high_engagement']:
            flag_reasons.append(f"High engagement ({profile['total_interactions']:,} interactions)")
            should_flag = True
        
        if profile.get('average_sentiment', 0) >= self.thresholds['positive_sentiment']:
            flag_reasons.append(f"Very positive sentiment ({profile['average_sentiment']:.1f}%)")
            should_flag = True
        
        if len(profile['platforms_analyzed']) >= self.thresholds['multi_platform']:
            flag_reasons.append(f"Multi-platform presence ({len(profile['platforms_analyzed'])} platforms)")
            should_flag = True
        
        # Special case: No social presence
        if not profile['platforms_analyzed']:
            flag_reasons.append("No social presence detected")
        
        return should_flag, flag_reasons
    
    def analyze_batch_applicants(self, applicants: List[Dict]) -> Dict:
        """
        Analyze multiple grant applicants in batch
        
        Args:
            applicants: List of applicant data dictionaries
            
        Returns:
            Batch analysis results with flagged applicants
        """
        results = {
            'total_applicants': len(applicants),
            'analyzed_applicants': 0,
            'flagged_applicants': [],
            'social_scores': [],
            'analysis_summary': {},
            'timestamp': datetime.now().isoformat()
        }
        
        for applicant in applicants:
            try:
                social_profile = self.analyze_grant_applicant(applicant)
                results['analyzed_applicants'] += 1
                results['social_scores'].append(social_profile['social_score'])
                
                if social_profile['flag_status']:
                    results['flagged_applicants'].append(social_profile)
                    
            except Exception as e:
                print(f"Error analyzing applicant {applicant.get('id', 'unknown')}: {e}")
        
        # Generate summary statistics
        if results['social_scores']:
            results['analysis_summary'] = {
                'average_social_score': round(sum(results['social_scores']) / len(results['social_scores']), 2),
                'max_social_score': max(results['social_scores']),
                'min_social_score': min(results['social_scores']),
                'flagged_percentage': round(len(results['flagged_applicants']) / results['analyzed_applicants'] * 100, 1)
            }
        
        # Sort flagged applicants by social score
        results['flagged_applicants'].sort(key=lambda x: x['social_score'], reverse=True)
        
        return results
    
    def generate_report(self, analysis_results: Dict) -> str:
        """
        Generate a human-readable analysis report
        
        Args:
            analysis_results: Results from analyze_batch_applicants
            
        Returns:
            Formatted report string
        """
        report = []
        report.append("🏆 STACKS DEGRANTS PHASE III - SOCIAL SCORE ANALYSIS")
        report.append("=" * 60)
        report.append(f"Analysis Date: {analysis_results['timestamp']}")
        report.append(f"Total Applicants: {analysis_results['total_applicants']}")
        report.append(f"Successfully Analyzed: {analysis_results['analyzed_applicants']}")
        
        if analysis_results['analysis_summary']:
            summary = analysis_results['analysis_summary']
            report.append(f"Average Social Score: {summary['average_social_score']}/100")
            report.append(f"Highest Social Score: {summary['max_social_score']}/100")
            report.append(f"Flagged Applicants: {len(analysis_results['flagged_applicants'])} ({summary['flagged_percentage']}%)")
        
        report.append("\n🚩 FLAGGED APPLICANTS (High Social Presence):")
        report.append("-" * 50)
        
        for i, applicant in enumerate(analysis_results['flagged_applicants'], 1):
            report.append(f"\n{i}. {applicant['applicant_name']} (ID: {applicant['applicant_id']})")
            report.append(f"   Social Score: {applicant['social_score']}/100")
            report.append(f"   Galaxy Score: {applicant.get('average_galaxy_score', 0):.1f}")
            report.append(f"   Total Interactions: {applicant['total_interactions']:,}")
            report.append(f"   Average Sentiment: {applicant.get('average_sentiment', 0):.1f}%")
            report.append(f"   Platforms: {', '.join(applicant['platforms_analyzed'])}")
            report.append(f"   Reasons: {'; '.join(applicant['flag_reasons'])}")
        
        return "\n".join(report)

def main():
    """Example usage of the Stacks DeGrants Analyzer"""
    try:
        analyzer = StacksDeGrantsAnalyzer()
        
        # Example grant applicants (replace with real data)
        sample_applicants = [
            {
                'id': 'GRANT_001',
                'name': 'Alice Blockchain',
                'social_handles': ['@alice_crypto', '@alice_dev', '@alice_stacks'],
                'project_description': 'DeFi protocol on Stacks'
            },
            {
                'id': 'GRANT_002',
                'name': 'Bob DeFi',
                'social_handles': ['@bob_defi', '@bob_builder'],
                'project_description': 'NFT marketplace'
            },
            {
                'id': 'GRANT_003',
                'name': 'Charlie Web3',
                'social_handles': ['@charlie_web3'],
                'project_description': 'Social media dApp'
            }
        ]
        
        print("🔍 Analyzing Stacks DeGrants applicants...")
        results = analyzer.analyze_batch_applicants(sample_applicants)
        
        print("\n" + analyzer.generate_report(results))
        
        # Save results to JSON file
        with open('stacks_degrants_analysis.json', 'w') as f:
            json.dump(results, f, indent=2)
        
        print(f"\n💾 Results saved to: stacks_degrants_analysis.json")
        
    except Exception as e:
        print(f"❌ Error: {e}")
        print("Make sure your LUNARCRUSH_API_KEY is set in the .env file")

if __name__ == "__main__":
    main()
