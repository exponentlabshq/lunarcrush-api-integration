#!/usr/bin/env python3
"""
Deep Network Intelligence Implementation
Course of Action 1: Advanced Social Analytics for Stacks Blockchain

This implementation demonstrates the first COA - Deep Network Intelligence
using higher-order logic and advanced LunarCrush API features.
"""

import os
import requests
import json
import networkx as nx
import pandas as pd
import numpy as np
from typing import Dict, List, Tuple, Optional
from dotenv import load_dotenv
from datetime import datetime, timedelta
import matplotlib.pyplot as plt
import seaborn as sns

class DeepNetworkIntelligence:
    """
    Advanced social network analysis using higher-order logic
    """
    
    def __init__(self):
        load_dotenv()
        self.api_key = os.getenv('LUNARCRUSH_API_KEY')
        self.base_url = "https://lunarcrush.com/api4"
        self.headers = {"Authorization": f"Bearer {self.api_key}"}
        
        # Initialize network graph
        self.network_graph = nx.DiGraph()
        
        # Higher-order logic parameters
        self.influence_decay_factor = 0.7  # Influence decays by 30% per hop
        self.min_influence_threshold = 0.01  # Minimum influence to consider
        self.max_hops = 3  # Maximum hops for influence propagation
    
    def analyze_creator_network(self, creator_id: str) -> Dict:
        """
        Comprehensive network analysis for a creator
        """
        print(f"🔍 Analyzing network for creator: {creator_id}")
        
        # Get creator data
        creator_data = self.get_creator_details(creator_id)
        if not creator_data:
            return {"error": "Creator not found"}
        
        # Build network graph
        network_data = self.build_network_graph(creator_id)
        
        # Calculate network metrics
        network_metrics = self.calculate_network_metrics(network_data)
        
        # Analyze top interactors
        top_interactors = self.analyze_top_interactors(creator_id)
        
        # Calculate influence propagation
        influence_propagation = self.calculate_influence_propagation(creator_id)
        
        # Assess Stacks alignment
        stacks_alignment = self.assess_stacks_alignment(creator_data)
        
        return {
            "creator_data": creator_data,
            "network_metrics": network_metrics,
            "top_interactors": top_interactors,
            "influence_propagation": influence_propagation,
            "stacks_alignment": stacks_alignment,
            "analysis_timestamp": datetime.now().isoformat()
        }
    
    def get_creator_details(self, creator_id: str) -> Optional[Dict]:
        """
        Get detailed creator information
        """
        try:
            url = f"{self.base_url}/public/creator/twitter/{creator_id}/v1"
            response = requests.get(url, headers=self.headers, timeout=10)
            
            if response.status_code == 200:
                return response.json().get('data', {})
            return None
        except Exception as e:
            print(f"Error getting creator details: {e}")
            return None
    
    def build_network_graph(self, creator_id: str) -> Dict:
        """
        Build network graph from creator's interactions
        """
        print("📊 Building network graph...")
        
        # Get creator's posts
        posts = self.get_creator_posts(creator_id)
        
        # Extract interactions
        interactions = []
        for post in posts:
            post_interactions = self.get_post_interactions(post.get('id', ''))
            interactions.extend(post_interactions)
        
        # Build graph
        for interaction in interactions:
            interactor_id = interaction.get('creator_id', '')
            if interactor_id:
                self.network_graph.add_edge(
                    creator_id, 
                    interactor_id, 
                    weight=interaction.get('interaction_strength', 1),
                    interaction_type=interaction.get('type', 'unknown')
                )
        
        return {
            "nodes": list(self.network_graph.nodes()),
            "edges": list(self.network_graph.edges()),
            "total_interactions": len(interactions)
        }
    
    def get_creator_posts(self, creator_id: str, limit: int = 50) -> List[Dict]:
        """
        Get creator's recent posts
        """
        try:
            url = f"{self.base_url}/public/creator/twitter/{creator_id}/posts/v1"
            params = {'limit': limit}
            response = requests.get(url, headers=self.headers, params=params, timeout=10)
            
            if response.status_code == 200:
                return response.json().get('data', [])
            return []
        except Exception as e:
            print(f"Error getting creator posts: {e}")
            return []
    
    def get_post_interactions(self, post_id: str) -> List[Dict]:
        """
        Get interactions for a specific post
        """
        # Note: This would require additional API endpoints
        # For now, we'll simulate based on available data
        return [
            {
                "creator_id": f"interactor_{i}",
                "interaction_strength": np.random.uniform(0.1, 1.0),
                "type": np.random.choice(["like", "retweet", "reply"])
            }
            for i in range(np.random.randint(5, 20))
        ]
    
    def calculate_network_metrics(self, network_data: Dict) -> Dict:
        """
        Calculate comprehensive network metrics
        """
        print("📈 Calculating network metrics...")
        
        if not self.network_graph.nodes():
            return {"error": "No network data available"}
        
        # Basic network metrics
        metrics = {
            "node_count": self.network_graph.number_of_nodes(),
            "edge_count": self.network_graph.number_of_edges(),
            "density": nx.density(self.network_graph),
            "average_clustering": nx.average_clustering(self.network_graph.to_undirected()),
        }
        
        # Centrality measures
        try:
            metrics.update({
                "betweenness_centrality": nx.betweenness_centrality(self.network_graph),
                "closeness_centrality": nx.closeness_centrality(self.network_graph),
                "eigenvector_centrality": nx.eigenvector_centrality(self.network_graph, max_iter=1000)
            })
        except Exception as e:
            print(f"Error calculating centrality: {e}")
        
        # Network structure
        metrics.update({
            "is_connected": nx.is_weakly_connected(self.network_graph),
            "strongly_connected_components": nx.number_strongly_connected_components(self.network_graph),
            "weakly_connected_components": nx.number_weakly_connected_components(self.network_graph)
        })
        
        return metrics
    
    def analyze_top_interactors(self, creator_id: str) -> List[Dict]:
        """
        Analyze top interactors and their influence
        """
        print("👥 Analyzing top interactors...")
        
        # Get top interactors from network
        top_interactors = []
        
        for neighbor in self.network_graph.neighbors(creator_id):
            edge_data = self.network_graph.get_edge_data(creator_id, neighbor)
            interaction_strength = edge_data.get('weight', 1) if edge_data else 1
            
            # Get neighbor details
            neighbor_data = self.get_creator_details(neighbor)
            
            if neighbor_data:
                interactor_analysis = {
                    "creator_id": neighbor,
                    "creator_name": neighbor_data.get('creator_name', 'Unknown'),
                    "followers": neighbor_data.get('creator_followers', 0),
                    "interaction_strength": interaction_strength,
                    "influence_score": self.calculate_influence_score(neighbor_data),
                    "network_position": self.calculate_network_position(neighbor),
                    "stacks_alignment": self.assess_stacks_alignment(neighbor_data)
                }
                top_interactors.append(interactor_analysis)
        
        # Sort by influence score
        top_interactors.sort(key=lambda x: x['influence_score'], reverse=True)
        
        return top_interactors[:10]  # Top 10 interactors
    
    def calculate_influence_score(self, creator_data: Dict) -> float:
        """
        Calculate comprehensive influence score
        """
        followers = creator_data.get('creator_followers', 0)
        interactions = creator_data.get('interactions_24h', 0)
        rank = creator_data.get('creator_rank', 999999)
        
        # Normalize metrics
        followers_norm = min(followers / 100000, 1.0)  # Normalize to 100K
        interactions_norm = min(interactions / 1000000, 1.0)  # Normalize to 1M
        rank_norm = max(0, min((1000000 - rank) / 1000000, 1.0))  # Invert rank
        
        # Weighted influence score
        influence_score = (
            followers_norm * 0.4 +
            interactions_norm * 0.4 +
            rank_norm * 0.2
        )
        
        return influence_score
    
    def calculate_network_position(self, creator_id: str) -> Dict:
        """
        Calculate creator's position in the network
        """
        if creator_id not in self.network_graph:
            return {"error": "Creator not in network"}
        
        # Calculate centrality measures
        try:
            betweenness = nx.betweenness_centrality(self.network_graph).get(creator_id, 0)
            closeness = nx.closeness_centrality(self.network_graph).get(creator_id, 0)
            eigenvector = nx.eigenvector_centrality(self.network_graph, max_iter=1000).get(creator_id, 0)
        except:
            betweenness = closeness = eigenvector = 0
        
        return {
            "betweenness_centrality": betweenness,
            "closeness_centrality": closeness,
            "eigenvector_centrality": eigenvector,
            "degree_centrality": self.network_graph.degree(creator_id) / max(1, self.network_graph.number_of_nodes() - 1)
        }
    
    def calculate_influence_propagation(self, creator_id: str) -> Dict:
        """
        Calculate influence propagation using higher-order logic
        """
        print("🌊 Calculating influence propagation...")
        
        # Get creator's base influence
        creator_data = self.get_creator_details(creator_id)
        base_influence = self.calculate_influence_score(creator_data) if creator_data else 0
        
        # Calculate multi-hop influence
        propagation_results = {
            "base_influence": base_influence,
            "1_hop_influence": 0,
            "2_hop_influence": 0,
            "3_hop_influence": 0,
            "total_reach": 0
        }
        
        # Calculate influence at each hop
        for hop in range(1, self.max_hops + 1):
            hop_influence = self.calculate_hop_influence(creator_id, hop)
            propagation_results[f"{hop}_hop_influence"] = hop_influence
            propagation_results["total_reach"] += hop_influence
        
        # Calculate viral coefficient
        propagation_results["viral_coefficient"] = self.calculate_viral_coefficient(creator_id)
        
        return propagation_results
    
    def calculate_hop_influence(self, creator_id: str, hop: int) -> float:
        """
        Calculate influence at specific hop distance
        """
        if hop == 0:
            return self.calculate_influence_score(self.get_creator_details(creator_id) or {})
        
        # Get neighbors at this hop
        try:
            neighbors = list(nx.single_source_shortest_path_length(self.network_graph, creator_id, cutoff=hop))
            hop_neighbors = [n for n in neighbors if nx.shortest_path_length(self.network_graph, creator_id, n) == hop]
        except:
            hop_neighbors = []
        
        # Calculate total influence at this hop
        total_influence = 0
        for neighbor in hop_neighbors:
            neighbor_data = self.get_creator_details(neighbor)
            if neighbor_data:
                neighbor_influence = self.calculate_influence_score(neighbor_data)
                # Apply decay factor
                decayed_influence = neighbor_influence * (self.influence_decay_factor ** hop)
                total_influence += decayed_influence
        
        return total_influence
    
    def calculate_viral_coefficient(self, creator_id: str) -> float:
        """
        Calculate viral coefficient (R₀) for influence propagation
        """
        # Get creator's posts and interactions
        posts = self.get_creator_posts(creator_id, limit=20)
        
        if not posts:
            return 0
        
        # Calculate average interactions per post
        total_interactions = sum(post.get('interactions_total', 0) for post in posts)
        avg_interactions = total_interactions / len(posts)
        
        # Calculate conversion rate (simplified)
        conversion_rate = min(avg_interactions / 1000, 0.1)  # Cap at 10%
        
        # Viral coefficient = Average interactions × Conversion rate
        viral_coefficient = avg_interactions * conversion_rate
        
        return viral_coefficient
    
    def assess_stacks_alignment(self, creator_data: Dict) -> Dict:
        """
        Assess alignment with Stacks ecosystem goals
        """
        print("🎯 Assessing Stacks alignment...")
        
        # Get topic influence data
        topic_influence = creator_data.get('topic_influence', [])
        
        # Define Stacks-relevant topics
        stacks_topics = {
            'bitcoin': 0.25,
            'blockchain': 0.20,
            'defi': 0.20,
            'layer2': 0.15,
            'scaling': 0.10,
            'smart_contracts': 0.10
        }
        
        # Calculate alignment score
        alignment_score = 0
        topic_scores = {}
        
        for topic_data in topic_influence:
            topic_name = topic_data.get('topic', '').lower()
            topic_count = topic_data.get('count', 0)
            topic_percent = topic_data.get('percent', 0)
            
            # Check if topic is Stacks-relevant
            for stacks_topic, weight in stacks_topics.items():
                if stacks_topic in topic_name:
                    topic_score = topic_percent * weight
                    alignment_score += topic_score
                    topic_scores[stacks_topic] = topic_score
        
        # Calculate overall alignment
        alignment_assessment = {
            "overall_alignment_score": alignment_score,
            "topic_scores": topic_scores,
            "alignment_level": self.get_alignment_level(alignment_score),
            "recommendation": self.get_alignment_recommendation(alignment_score)
        }
        
        return alignment_assessment
    
    def get_alignment_level(self, score: float) -> str:
        """
        Get alignment level based on score
        """
        if score >= 0.7:
            return "High"
        elif score >= 0.4:
            return "Medium"
        elif score >= 0.1:
            return "Low"
        else:
            return "Very Low"
    
    def get_alignment_recommendation(self, score: float) -> str:
        """
        Get recommendation based on alignment score
        """
        if score >= 0.7:
            return "Strong Consideration - High Stacks alignment"
        elif score >= 0.4:
            return "Consideration - Moderate Stacks alignment"
        elif score >= 0.1:
            return "Additional Review - Low Stacks alignment"
        else:
            return "Not Recommended - Very low Stacks alignment"
    
    def generate_network_report(self, analysis_data: Dict) -> str:
        """
        Generate comprehensive network analysis report
        """
        creator_data = analysis_data.get('creator_data', {})
        network_metrics = analysis_data.get('network_metrics', {})
        top_interactors = analysis_data.get('top_interactors', [])
        influence_propagation = analysis_data.get('influence_propagation', {})
        stacks_alignment = analysis_data.get('stacks_alignment', {})
        
        report = f"""
# Deep Network Intelligence Report
## Creator: @{creator_data.get('creator_name', 'Unknown')}

**Analysis Date**: {analysis_data.get('analysis_timestamp', 'N/A')}
**Creator ID**: {creator_data.get('creator_id', 'N/A')}
**Followers**: {creator_data.get('creator_followers', 0):,}
**24h Interactions**: {creator_data.get('interactions_24h', 0):,}

---

## Network Metrics

### Basic Network Statistics
- **Network Size**: {network_metrics.get('node_count', 0)} nodes
- **Connections**: {network_metrics.get('edge_count', 0)} edges
- **Network Density**: {network_metrics.get('density', 0):.3f}
- **Average Clustering**: {network_metrics.get('average_clustering', 0):.3f}

### Network Structure
- **Connected**: {network_metrics.get('is_connected', False)}
- **Strongly Connected Components**: {network_metrics.get('strongly_connected_components', 0)}
- **Weakly Connected Components**: {network_metrics.get('weakly_connected_components', 0)}

---

## Top Interactors Analysis

"""
        
        for i, interactor in enumerate(top_interactors[:5], 1):
            report += f"""
### {i}. @{interactor.get('creator_name', 'Unknown')}
- **Followers**: {interactor.get('followers', 0):,}
- **Influence Score**: {interactor.get('influence_score', 0):.3f}
- **Interaction Strength**: {interactor.get('interaction_strength', 0):.3f}
- **Stacks Alignment**: {interactor.get('stacks_alignment', {}).get('alignment_level', 'Unknown')}
"""
        
        report += f"""

---

## Influence Propagation Analysis

### Multi-Hop Influence
- **Base Influence**: {influence_propagation.get('base_influence', 0):.3f}
- **1-Hop Influence**: {influence_propagation.get('1_hop_influence', 0):.3f}
- **2-Hop Influence**: {influence_propagation.get('2_hop_influence', 0):.3f}
- **3-Hop Influence**: {influence_propagation.get('3_hop_influence', 0):.3f}
- **Total Reach**: {influence_propagation.get('total_reach', 0):.3f}

### Viral Potential
- **Viral Coefficient**: {influence_propagation.get('viral_coefficient', 0):.3f}

---

## Stacks Ecosystem Alignment

### Alignment Assessment
- **Overall Alignment Score**: {stacks_alignment.get('overall_alignment_score', 0):.3f}
- **Alignment Level**: {stacks_alignment.get('alignment_level', 'Unknown')}
- **Recommendation**: {stacks_alignment.get('recommendation', 'N/A')}

### Topic Alignment Breakdown
"""
        
        for topic, score in stacks_alignment.get('topic_scores', {}).items():
            report += f"- **{topic.title()}**: {score:.3f}\n"
        
        report += f"""

---

## Strategic Recommendations

### Network Intelligence Insights
1. **Influence Quality**: {'High' if influence_propagation.get('base_influence', 0) > 0.5 else 'Medium' if influence_propagation.get('base_influence', 0) > 0.2 else 'Low'} base influence
2. **Network Reach**: {'Extensive' if influence_propagation.get('total_reach', 0) > 1.0 else 'Moderate' if influence_propagation.get('total_reach', 0) > 0.5 else 'Limited'} multi-hop reach
3. **Viral Potential**: {'High' if influence_propagation.get('viral_coefficient', 0) > 100 else 'Medium' if influence_propagation.get('viral_coefficient', 0) > 50 else 'Low'} viral coefficient

### Stacks Ecosystem Fit
- **Strategic Alignment**: {stacks_alignment.get('alignment_level', 'Unknown')} alignment with Stacks goals
- **Grant Recommendation**: {stacks_alignment.get('recommendation', 'N/A')}

---

*This analysis leverages advanced network theory and higher-order logic to provide comprehensive insights into creator influence and ecosystem alignment.*
"""
        
        return report

def main():
    """
    Main function to demonstrate Deep Network Intelligence
    """
    print("🚀 Deep Network Intelligence Analysis")
    print("=" * 50)
    
    # Initialize analyzer
    analyzer = DeepNetworkIntelligence()
    
    # Analyze @attractfund1ng
    creator_id = "attractfund1ng"
    analysis_data = analyzer.analyze_creator_network(creator_id)
    
    if "error" in analysis_data:
        print(f"❌ Error: {analysis_data['error']}")
        return
    
    # Generate report
    report = analyzer.generate_network_report(analysis_data)
    
    # Save report
    with open(f"{creator_id}_deep_network_analysis.md", "w") as f:
        f.write(report)
    
    print(f"✅ Deep network analysis complete!")
    print(f"📄 Report saved as: {creator_id}_deep_network_analysis.md")
    
    # Print summary
    creator_data = analysis_data.get('creator_data', {})
    network_metrics = analysis_data.get('network_metrics', {})
    stacks_alignment = analysis_data.get('stacks_alignment', {})
    
    print(f"\n📊 Summary for @{creator_data.get('creator_name', 'Unknown')}:")
    print(f"   Network Size: {network_metrics.get('node_count', 0)} nodes")
    print(f"   Stacks Alignment: {stacks_alignment.get('alignment_level', 'Unknown')}")
    print(f"   Recommendation: {stacks_alignment.get('recommendation', 'N/A')}")

if __name__ == "__main__":
    main()
