# LunarCrush API v4
Base URL: https://lunarcrush.com/api4  
Authentication: <https://lunarcrush.com/developers/api/authentication>  
Available Endpoints:

**Topics**  
[Topics List](#topics-list)  
[Topic Whatsup](#topic-whatsup)  
[Topic](#topic)  
[Topic Time Series v2](#topic-time-series-v2)  
[Topic Time Series](#topic-time-series)  
[Topic Posts](#topic-posts)  
[Topic News](#topic-news)  
[Topic Creators](#topic-creators)  
**Categories**  
[Category](#category)  
[Category Topics](#category-topics)  
[Category Time Series](#category-time-series)  
[Category Posts](#category-posts)  
[Category News](#category-news)  
[Category Creators](#category-creators)  
[Categories List](#categories-list)  
**Creators**  
[Creators List](#creators-list)  
[Creator](#creator)  
[Creator Time Series](#creator-time-series)  
[Creator Posts](#creator-posts)  
**Posts**  
[Posts](#posts)  
[Posts Time Series](#posts-time-series)  
**Coins**  
[Coins List v2](#coins-list-v2)  
[Coins List](#coins-list)  
[Coins](#coins)  
[Coins Time Series](#coins-time-series)  
[Coins Meta](#coins-meta)  
**Stocks**  
[Stocks List v2](#stocks-list-v2)  
[Stocks List](#stocks-list)  
[Stocks](#stocks)  
[Stocks Time Series](#stocks-time-series)  
**Searches**  
[Searches Search](#searches-search)  
[Searches List](#searches-list)  
[Searches Create](#searches-create)  
[Searches Update](#searches-update)  
[Searches Delete](#searches-delete)  
[Searches](#searches)  
**Systems**  
[System Changes](#system-changes)  






---

### Topics List

https://lunarcrush.com/api4/public/topics/list/v1

Get a list of trending social topics.

Example request:

```bash
curl -H "Authorization: Bearer <API_KEY>" https://lunarcrush.com/api4/public/topics/list/v1
```



Example response:

```json
{
  "data": [
    {
      "topic": "youtube",
      "title": "YouTube",
      "topic_rank": 1,
      "topic_rank_1h_previous": 1,
      "topic_rank_24h_previous": 1,
      "num_contributors": 335952,
      "num_posts": 733220,
      "interactions_24h": 3296046298
    }
  ]
}
```

Schema:

+ **topic**: LunarCrush social topic. Can only includes letters, numbers, spaces, #, and $
+ **title**: The case sensitive title of the topic or category
+ **topic_rank**: LunarCrush metric for ranking a social topic relative to all other social topics
+ **topic_rank_1h_previous**: The topic rank from 1 hour ago
+ **topic_rank_24h_previous**: The topic rank from 24 hours ago
+ **num_contributors**: The number of unique social contributors to the topic
+ **num_posts**: Total number of posts with interactions on this topic in the last 24 hours
+ **interactions_24h**: Number of interactions in the last 24 hours




---

### Topic Whatsup

https://lunarcrush.com/api4/public/topic/:topic/whatsup/v1

Generate an AI summary of the hottest news and social posts for a specific topic

input parameters:

+ **topic**: _Provide the topic to get a summary for. A topic must be all lower case and can only include letters, numbers, spaces, # and $._ **required**

Example request:

```bash
curl -H "Authorization: Bearer <API_KEY>" https://lunarcrush.com/api4/public/topic/bitcoin/whatsup/v1
```



Example response:

```json
{
  "config": {
    "topic": "bitcoin",
    "generated": 1760641738
  },
  "summary": "Florida has introduced a new bill to establish Bitcoin and digital asset reserves, while BlackRock's CEO has taken back anti-Bitcoin comments, saying markets force investors to relook at their assumptions. Meanwhile, Bitcoin miners have deposited 51,000 BTC to Binance since October 9, and traders are betting on a potential crash. Several major companies, including Steak 'n Shake and Compass Coffee, have made recent announcements related to Bitcoin adoption."
}
```

Schema:

+ **config**: This includes the inputs for the request processed by the server and may include additional hints about the request and response information.
+ **topic**: LunarCrush social topic. Can only includes letters, numbers, spaces, #, and $
+ **generated**: A unix timestamp (in seconds) when the data was generated to understand possibly stale data




---

### Topic

https://lunarcrush.com/api4/public/topic/:topic/v1

Get summary information for a social topic. The output is a 24 hour aggregation social activity with metrics comparing the latest 24 hours to the previous 24 hours.

input parameters:

+ **topic**: _Provide the topic to get details for. A topic must be all lower case and can only include letters, numbers, spaces, # and $. You can also look up a topic by the coin/nft/stock numeric id like coins:1 for bitcoin or stocks:7056 for nVidia._ **required**

Example request:

```bash
curl -H "Authorization: Bearer <API_KEY>" https://lunarcrush.com/api4/public/topic/bitcoin/v1
```



Example response:

```json
{
  "config": {
    "id": "bitcoin",
    "name": "Bitcoin",
    "symbol": "BTC",
    "topic": "bitcoin",
    "generated": 1760647718
  },
  "data": {
    "topic": "bitcoin",
    "title": "Bitcoin",
    "topic_rank": 20,
    "related_topics": [
      "coins layer 1"
    ],
    "types_count": {
      "tweet": 541993,
      "news": 2261,
      "reddit-post": 1779,
      "tiktok-video": 26445,
      "youtube-video": 53667
    },
    "types_interactions": {
      "tweet": 149892441,
      "news": 474337,
      "reddit-post": 222222,
      "tiktok-video": 14301525,
      "youtube-video": 18352885
    },
    "types_sentiment": {
      "tweet": 76,
      "news": 73,
      "reddit-post": 69,
      "tiktok-video": 67,
      "youtube-video": 77
    },
    "types_sentiment_detail": {
      "tweet": {
        "positive": 65264670,
        "neutral": 57398540,
        "negative": 27229231
      },
      "news": {
        "positive": 214544,
        "neutral": 178775,
        "negative": 81018
      },
      "reddit-post": {
        "positive": 32739,
        "neutral": 148293,
        "negative": 41190
      },
      "tiktok-video": {
        "positive": 4305587,
        "neutral": 8045071,
        "negative": 1950867
      },
      "youtube-video": {
        "positive": 7256198,
        "neutral": 8908297,
        "negative": 2188390
      }
    },
    "interactions_24h": 183243410,
    "num_contributors": 91070,
    "num_posts": 353615,
    "categories": [
      "Cryptocurrencies"
    ],
    "trend": "flat"
  }
}
```

Schema:

+ **config**: This includes the inputs for the request processed by the server and may include additional hints about the request and response information.
+ **id**: LunarCrush internal ID for the asset
+ **name**: The full name of the asset
+ **symbol**: The symbol for the asset
+ **topic**: LunarCrush social topic. Can only includes letters, numbers, spaces, #, and $
+ **generated**: A unix timestamp (in seconds) when the data was generated to understand possibly stale data
+ **title**: The case sensitive title of the topic or category
+ **topic_rank**: LunarCrush metric for ranking a social topic relative to all other social topics
+ **related_topics**: an array of related topics
+ **types_count**: An object with the counts of the total number of unique posts getting interactions from each social network in the last 24 hours
+ **types_interactions**: An object with the counts of the total number of interactions on each post from each social network in the last 24 hours
+ **types_sentiment**: An object with the sentiment score broken down by each supported social network. 0% is all posts negative, 100% is all posts positive. 50% is equal positive and negative posts. Each post is weighted by interactions.
+ **types_sentiment_detail**: An object with the breakdown of positive, neutral, and negative posts by 24h interactions for each social network
+ **interactions_24h**: Number of interactions in the last 24 hours
+ **num_contributors**: The number of unique social contributors to the topic
+ **num_posts**: Total number of posts with interactions on this topic in the last 24 hours
+ **categories**: an array of categories this topic aggregates into
+ **trend**: One of up, down or flat to represent the general trend in interactions




---

### Topic Time Series v2

https://lunarcrush.com/api4/public/topic/:topic/time-series/v2

Get historical time series data for a social topic

input parameters:

+ **topic**: _Provide the topic to get details for. A topic must be all lower case and can only include letters, numbers, spaces, # and $._ **required**
+ **bucket**: _Leave blank (default) for the most week aggregated by hour, specify hour for full historical data available in hourly aggregation, specify day for full historical data available in daily aggregation._ 

Example request:

```bash
curl -H "Authorization: Bearer <API_KEY>" https://lunarcrush.com/api4/public/topic/bitcoin/time-series/v2
```



Example response:

```json
{
  "config": {
    "topic": "bitcoin",
    "id": "bitcoin",
    "name": "Bitcoin",
    "symbol": "BTC",
    "interval": "1w",
    "start": 1759968000,
    "end": 1760654918,
    "bucket": "hour",
    "metrics": [],
    "generated": 1760647718
  },
  "data": [
    {
      "time": 1759968000,
      "contributors_active": 30745,
      "contributors_created": 1810,
      "interactions": 3972578,
      "posts_active": 62957,
      "posts_created": 2440,
      "sentiment": 78,
      "spam": 339,
      "alt_rank": 198,
      "circulating_supply": 19931834,
      "close": 123004.71,
      "galaxy_score": 56,
      "high": 123004.71,
      "low": 122931.87,
      "market_cap": 2453542301616,
      "market_dominance": 58.0797,
      "open": 123004.71,
      "social_dominance": 30.3039,
      "volume_24h": 62979418928
    }
  ]
}
```

Schema:

+ **config**: This includes the inputs for the request processed by the server and may include additional hints about the request and response information.
+ **topic**: LunarCrush social topic. Can only includes letters, numbers, spaces, #, and $
+ **id**: LunarCrush internal ID for the asset
+ **name**: The full name of the asset
+ **symbol**: The symbol for the asset
+ **interval**: Typically used for specifying time intervals like 1w = 1 week, 1m = 1 month etc
+ **start**: Start/from unix timestamp (in seconds)
+ **end**: End/to unix timestamp (in seconds)
+ **bucket**: Data is generally bucketed into hours or days
+ **metrics**: Comma separated list of metrics to include or that are included
+ **generated**: A unix timestamp (in seconds) when the data was generated to understand possibly stale data
+ **time**: A unix timestamp (in seconds)
+ **contributors_active**: number of unique social accounts with posts that have interactions
+ **contributors_created**: number of unique social accounts that created new posts
+ **interactions**: number of all publicly measurable interactions on a social post (views, likes, comments, thumbs up, upvote, share etc)
+ **posts_active**: number of unique social posts with interactions
+ **posts_created**: number of unique social posts created
+ **sentiment**: % of posts (weighted by interactions) that are positive. 100% means all posts are positive, 50% is half positive and half negative, and 0% is all negative posts.
+ **spam**: The number of posts created that are considered spam
+ **alt_rank**: A proprietary score based on how an asset is performing relative to all other assets supported
+ **circulating_supply**: Circulating Supply is the total number of coins or tokens that are actively available for trade and are being used in the market and in general public
+ **close**: Close price for the time period
+ **galaxy_score**: A proprietary score based on technical indicators of price, average social sentiment, relative social activity, and a factor of how closely social indicators correlate with price and volume
+ **high**: Higest price fo rthe time period
+ **low**: Lowest price for the time period
+ **market_cap**: Total dollar market value of all circulating supply or outstanding shares
+ **market_dominance**: The percent of the total market cap that this asset represents
+ **open**: Open price for the time period
+ **social_dominance**: The percent of the total social volume that this topic represents
+ **volume_24h**: Volume in USD for 24 hours up to this data point




---

### Topic Time Series

https://lunarcrush.com/api4/public/topic/:topic/time-series/v1

Get historical time series data for a social topic

input parameters:

+ **topic**: _Provide the topic to get details for. A topic must be all lower case and can only include letters, numbers, spaces, # and $._ **required**
+ **bucket**: _bucket time series data into hours or days. default is hours._ 
+ **interval**: _Use interval to specify the start and end time automatically for convenience. If "start" or "end" parameters are provided this parameter is ignored._ 
+ **start**: _The start time (unix timestamp) to go back to._ 
+ **end**: _The end time (unix timestamp) to stop at._ 

Example request:

```bash
curl -H "Authorization: Bearer <API_KEY>" https://lunarcrush.com/api4/public/topic/bitcoin/time-series/v1
```



Example response:

```json
{
  "config": {
    "topic": "bitcoin",
    "id": "bitcoin",
    "name": "Bitcoin",
    "symbol": "BTC",
    "interval": "1w",
    "start": 1759968000,
    "end": 1760654918,
    "bucket": "hour",
    "metrics": [],
    "generated": 1760647718
  },
  "data": [
    {
      "time": 1759968000,
      "contributors_active": 30745,
      "contributors_created": 1810,
      "interactions": 3972578,
      "posts_active": 62957,
      "posts_created": 2440,
      "sentiment": 78,
      "spam": 339,
      "alt_rank": 198,
      "circulating_supply": 19931834,
      "close": 123004.71,
      "galaxy_score": 56,
      "high": 123004.71,
      "low": 122931.87,
      "market_cap": 2453542301616,
      "market_dominance": 58.0797,
      "open": 123004.71,
      "social_dominance": 30.3039,
      "volume_24h": 62979418928
    }
  ]
}
```

Schema:

+ **config**: This includes the inputs for the request processed by the server and may include additional hints about the request and response information.
+ **topic**: LunarCrush social topic. Can only includes letters, numbers, spaces, #, and $
+ **id**: LunarCrush internal ID for the asset
+ **name**: The full name of the asset
+ **symbol**: The symbol for the asset
+ **interval**: Typically used for specifying time intervals like 1w = 1 week, 1m = 1 month etc
+ **start**: Start/from unix timestamp (in seconds)
+ **end**: End/to unix timestamp (in seconds)
+ **bucket**: Data is generally bucketed into hours or days
+ **metrics**: Comma separated list of metrics to include or that are included
+ **generated**: A unix timestamp (in seconds) when the data was generated to understand possibly stale data
+ **time**: A unix timestamp (in seconds)
+ **contributors_active**: number of unique social accounts with posts that have interactions
+ **contributors_created**: number of unique social accounts that created new posts
+ **interactions**: number of all publicly measurable interactions on a social post (views, likes, comments, thumbs up, upvote, share etc)
+ **posts_active**: number of unique social posts with interactions
+ **posts_created**: number of unique social posts created
+ **sentiment**: % of posts (weighted by interactions) that are positive. 100% means all posts are positive, 50% is half positive and half negative, and 0% is all negative posts.
+ **spam**: The number of posts created that are considered spam
+ **alt_rank**: A proprietary score based on how an asset is performing relative to all other assets supported
+ **circulating_supply**: Circulating Supply is the total number of coins or tokens that are actively available for trade and are being used in the market and in general public
+ **close**: Close price for the time period
+ **galaxy_score**: A proprietary score based on technical indicators of price, average social sentiment, relative social activity, and a factor of how closely social indicators correlate with price and volume
+ **high**: Higest price fo rthe time period
+ **low**: Lowest price for the time period
+ **market_cap**: Total dollar market value of all circulating supply or outstanding shares
+ **market_dominance**: The percent of the total market cap that this asset represents
+ **open**: Open price for the time period
+ **social_dominance**: The percent of the total social volume that this topic represents
+ **volume_24h**: Volume in USD for 24 hours up to this data point




---

### Topic Posts

https://lunarcrush.com/api4/public/topic/:topic/posts/v1

Get the top posts for a social topic. If start time is provided the result will be the top posts by interactions for the time range. If start is not provided it will be the most recent top posts by interactions from the last 24 hours.

input parameters:

+ **topic**: _Provide the topic to get details for. A topic must be all lower case and can only include letters, numbers, spaces, # and $._ **required**
+ **start**: _The start time (unix timestamp) to start at. Will be rounded to the beginning of the day. If the end parameter is not provided it will just be the top posts for this day._ 
+ **end**: _(Optional) The end time (unix timestamp) to stop at. Will be rounded to the end of the day._ 

Example request:

```bash
curl -H "Authorization: Bearer <API_KEY>" https://lunarcrush.com/api4/public/topic/bitcoin/posts/v1
```



Example response:

```json
{
  "config": {
    "topic": "bitcoin",
    "type": "topic",
    "id": "bitcoin",
    "name": "Bitcoin",
    "symbol": "BTC",
    "generated": 1760647718
  },
  "data": [
    {
      "id": "t3_1o7u058",
      "post_type": "reddit-post",
      "post_title": "Made this bitcoin shadow box. Not sure if I'm crazy about this design but it's something",
      "post_link": "https://redd.it/1o7u058",
      "post_image": null,
      "post_created": 1760646307,
      "post_sentiment": 3.2,
      "creator_id": "reddit::t2_kszqkqvk",
      "creator_name": "Outrageous-Garage179",
      "creator_display_name": "Outrageous-Garage179",
      "creator_avatar": "https://styles.redditmedia.com/t5_60m8fu/styles/profileIcon_63j7drb563fa1.png?width=256&height=256&crop=256:256,smart&s=9b79b5074a344e0e8cf39a127dcfa5c2f4b5ecf3",
      "interactions_24h": 1683,
      "interactions_total": 1683
    }
  ]
}
```

Schema:

+ **config**: This includes the inputs for the request processed by the server and may include additional hints about the request and response information.
+ **topic**: LunarCrush social topic. Can only includes letters, numbers, spaces, #, and $
+ **type**: Type of item or social network of item e.g. tweet, youtube-video, tiktok, x, youtube, category, topic, creator/influencer
+ **id**: Unique id of the social post
+ **name**: The full name of the asset
+ **symbol**: The symbol for the asset
+ **generated**: A unix timestamp (in seconds) when the data was generated to understand possibly stale data
+ **post_type**: The type of social post
+ **post_title**: The title text of the social post
+ **post_link**: The URL to view the social post on the social network
+ **post_image**: The URL to the primary image for the post if available
+ **post_created**: The unix timestamp of our best indication of when the post was created
+ **post_sentiment**: The sentiment of the post is a score between 1 and 5 with 1 being very negative, 3 being neutral, and 5 being very positive. A score of 3.5 is considered slightly positive.
+ **creator_id**: The [network]::[unique_id] for the influencer
+ **creator_name**: The unique screen name for the influencer
+ **creator_display_name**: The chosen display name for the influencer if available
+ **creator_avatar**: The URL to the avatar for the creator
+ **interactions_24h**: Number of interactions in the last 24 hours
+ **interactions_total**: Number of total interactions




---

### Topic News

https://lunarcrush.com/api4/public/topic/:topic/news/v1

Get the top news posts for a social topic. Top news is determined by the metrics related to the social posts that mention the news posts.

input parameters:

+ **topic**: _Provide the topic to get details for. A topic must be all lower case and can only include letters, numbers, spaces, # and $._ **required**

Example request:

```bash
curl -H "Authorization: Bearer <API_KEY>" https://lunarcrush.com/api4/public/topic/bitcoin/news/v1
```



Example response:

```json
{
  "config": {
    "topic": "bitcoin",
    "type": "topic",
    "id": "bitcoin",
    "name": "Bitcoin",
    "symbol": "BTC",
    "generated": 1760647719
  },
  "data": [
    {
      "id": "investing.com-4286876853",
      "post_type": "news",
      "post_title": "Newsmax board authorizes up to $5 million in Bitcoin and Trump Coin purchases By Investing.com",
      "post_link": "https://www.investing.com/news/cryptocurrency-news/newsmax-board-authorizes-up-to-5-million-in-bitcoin-and-trump-coin-purchases-432SI-4293113",
      "post_image": "https://i-invdn-com.investing.com/news/LYNXNPEE880S2_L.jpg",
      "post_created": 1760645592,
      "post_sentiment": 3.13,
      "creator_id": "twitter::988955288",
      "creator_name": "Investingcom",
      "creator_display_name": "Investing.com",
      "creator_followers": 1313131,
      "creator_avatar": "https://pbs.twimg.com/profile_images/1110172882368368640/pUSI1yPZ_200x200.png",
      "interactions_24h": 56,
      "interactions_total": 56
    }
  ]
}
```

Schema:

+ **config**: This includes the inputs for the request processed by the server and may include additional hints about the request and response information.
+ **topic**: LunarCrush social topic. Can only includes letters, numbers, spaces, #, and $
+ **type**: Type of item or social network of item e.g. tweet, youtube-video, tiktok, x, youtube, category, topic, creator/influencer
+ **id**: LunarCrush internal ID for the asset
+ **name**: The full name of the asset
+ **symbol**: The symbol for the asset
+ **generated**: A unix timestamp (in seconds) when the data was generated to understand possibly stale data
+ **post_type**: The type of social post
+ **post_title**: The title text of the social post
+ **post_link**: The URL to view the social post on the social network
+ **post_image**: The URL to the primary image for the post if available
+ **post_created**: The unix timestamp of our best indication of when the post was created
+ **post_sentiment**: The sentiment of the post is a score between 1 and 5 with 1 being very negative, 3 being neutral, and 5 being very positive. A score of 3.5 is considered slightly positive.
+ **creator_id**: The [network]::[unique_id] for the influencer
+ **creator_name**: The unique screen name for the influencer
+ **creator_display_name**: The chosen display name for the influencer if available
+ **creator_followers**: number of followers the account has
+ **creator_avatar**: The URL to the avatar for the creator
+ **interactions_24h**: Number of interactions in the last 24 hours
+ **interactions_total**: Number of total interactions




---

### Topic Creators

https://lunarcrush.com/api4/public/topic/:topic/creators/v1

Get the top creators for a social topic

input parameters:

+ **topic**: _Provide the topic to get details for. A topic must be all lower case and can only include letters, numbers, spaces, # and $._ **required**

Example request:

```bash
curl -H "Authorization: Bearer <API_KEY>" https://lunarcrush.com/api4/public/topic/bitcoin/creators/v1
```



Example response:

```json
{
  "data": [
    {
      "creator_id": "tiktok::7509870025967207447",
      "creator_name": "yeti.solana",
      "creator_avatar": "https://p16-sign-va.tiktokcdn.com/tos-maliva-avt-0068/93e1598920b075388436ef3aa00fb2b9~tplv-tiktokx-cropcenter:100:100.webp?dr=14579&refresh_token=7404bb29&x-expires=1760720400&x-signature=zGB30r6Ns86%2FC7fxbCIOGusQlnA%3D&t=4d5b0474&ps=13740610&shp=d05b14bd&shcp=34ff8df6&idc=sg1",
      "creator_followers": 353382,
      "creator_rank": 1,
      "interactions_24h": 3074146
    }
  ]
}
```

Schema:

+ **creator_id**: The [network]::[unique_id] for the influencer
+ **creator_name**: The unique screen name for the influencer
+ **creator_avatar**: The URL to the avatar for the creator
+ **creator_followers**: number of followers the account has
+ **creator_rank**: ranking based on all posts in the last 24 hours that have interactions
+ **interactions_24h**: Number of interactions in the last 24 hours




---

### Category

https://lunarcrush.com/api4/public/category/:category/v1

Get summary information for a social category

input parameters:

+ **category**: _Provide the category to get details for. A category must be all lower case and can only include letters, numbers, and spaces. A category is the aggregation of all posts for all topics within the category._ **required**

Example request:

```bash
curl -H "Authorization: Bearer <API_KEY>" https://lunarcrush.com/api4/public/category/musicians/v1
```



Example response:

```json
{
  "data": {
    "topic": "_musicians",
    "title": "Musicians",
    "related_topics": [
      "aerosmith"
    ],
    "types_count": {
      "news": 1782,
      "reddit-post": 3864,
      "tweet": 283820,
      "youtube-video": 255909,
      "tiktok-video": 82185
    },
    "types_interactions": {
      "news": 3238256,
      "reddit-post": 852299,
      "tweet": 294166627,
      "youtube-video": 1103401779,
      "tiktok-video": 543971929
    },
    "types_sentiment": {
      "news": 88,
      "reddit-post": 71,
      "tweet": 71,
      "youtube-video": 72,
      "tiktok-video": 75
    },
    "types_sentiment_detail": {
      "news": {
        "positive": 2696753,
        "neutral": 340229,
        "negative": 201274
      },
      "reddit-post": {
        "positive": 216442,
        "neutral": 441558,
        "negative": 194299
      },
      "tweet": {
        "positive": 127416210,
        "neutral": 118003919,
        "negative": 48746498
      },
      "youtube-video": {
        "positive": 341223354,
        "neutral": 632124032,
        "negative": 130054393
      },
      "tiktok-video": {
        "positive": 176233535,
        "neutral": 312390002,
        "negative": 55348392
      }
    },
    "interactions_24h": 1945630890,
    "num_contributors": 222096,
    "num_posts": 409185,
    "trend": "flat"
  }
}
```

Schema:

+ **topic**: LunarCrush social topic. Can only includes letters, numbers, spaces, #, and $
+ **title**: The case sensitive title of the topic or category
+ **related_topics**: an array of related topics
+ **types_count**: An object with the counts of the total number of unique posts getting interactions from each social network in the last 24 hours
+ **types_interactions**: An object with the counts of the total number of interactions on each post from each social network in the last 24 hours
+ **types_sentiment**: An object with the sentiment score broken down by each supported social network. 0% is all posts negative, 100% is all posts positive. 50% is equal positive and negative posts. Each post is weighted by interactions.
+ **types_sentiment_detail**: An object with the breakdown of positive, neutral, and negative posts by 24h interactions for each social network
+ **interactions_24h**: Number of interactions in the last 24 hours
+ **num_contributors**: The number of unique social contributors to the topic
+ **num_posts**: Total number of posts with interactions on this topic in the last 24 hours
+ **trend**: One of up, down or flat to represent the general trend in interactions




---

### Category Topics

https://lunarcrush.com/api4/public/category/:category/topics/v1

Get the top topics for a social category

input parameters:

+ **category**: _Provide the topic to get details for. A topic must be all lower case and can only include letters, numbers, spaces, # and $._ **required**

Example request:

```bash
curl -H "Authorization: Bearer <API_KEY>" https://lunarcrush.com/api4/public/category/musicians/topics/v1
```



Example response:

```json
{
  "data": [
    {
      "topic": 3038,
      "title": "Aerosmith",
      "topic_rank": 2823,
      "topic_rank_1h_previous": 1644,
      "topic_rank_24h_previous": 2574,
      "num_contributors": 1262,
      "social_dominance": 0.18415948882378766,
      "num_posts": 2019,
      "interactions_24h": 3755483
    }
  ]
}
```

Schema:

+ **topic**: LunarCrush social topic. Can only includes letters, numbers, spaces, #, and $
+ **title**: The case sensitive title of the topic or category
+ **topic_rank**: LunarCrush metric for ranking a social topic relative to all other social topics
+ **topic_rank_1h_previous**: The topic rank from 1 hour ago
+ **topic_rank_24h_previous**: The topic rank from 24 hours ago
+ **num_contributors**: The number of unique social contributors to the topic
+ **social_dominance**: The percent of the total social volume that this topic represents
+ **num_posts**: Total number of posts with interactions on this topic in the last 24 hours
+ **interactions_24h**: Number of interactions in the last 24 hours




---

### Category Time Series

https://lunarcrush.com/api4/public/category/:category/time-series/v1

Get historical time series data for a social category

input parameters:

+ **category**: _Provide the category to get details for. A category must be all lower case and can only include letters, numbers, and spaces._ **required**
+ **bucket**: _bucket time series data into hours or days. default is hours._ 
+ **interval**: _Use interval to specify the start and end time automatically for convenience. If "start" or "end" parameters are provided this parameter is ignored._ 
+ **start**: _The start time (unix timestamp) to go back to._ 
+ **end**: _The end time (unix timestamp) to stop at._ 

Example request:

```bash
curl -H "Authorization: Bearer <API_KEY>" https://lunarcrush.com/api4/public/category/cryptocurrencies/time-series/v1
```



Example response:

```json
{
  "config": {
    "category": "cryptocurrencies",
    "topic": "_cryptocurrencies",
    "type": "topic",
    "id": "_cryptocurrencies",
    "interval": "1w",
    "start": 1759968000,
    "end": 1760654920,
    "bucket": "hour",
    "metrics": [],
    "remote_api": "danode2-13",
    "generated": 1760647720
  },
  "data": [
    {
      "time": 1759968000,
      "contributors_active": 89673,
      "contributors_created": 4712,
      "interactions": 11441299,
      "posts_active": 207752,
      "posts_created": 6879,
      "sentiment": 79,
      "spam": 672
    }
  ]
}
```

Schema:

+ **config**: This includes the inputs for the request processed by the server and may include additional hints about the request and response information.
+ **category**: LunarCrush social category. Can only includes letters, numbers and spaces
+ **topic**: LunarCrush social topic. Can only includes letters, numbers, spaces, #, and $
+ **type**: Type of item or social network of item e.g. tweet, youtube-video, tiktok, x, youtube, category, topic, creator/influencer
+ **id**: LunarCrush internal ID for the asset
+ **interval**: Typically used for specifying time intervals like 1w = 1 week, 1m = 1 month etc
+ **start**: Start/from unix timestamp (in seconds)
+ **end**: End/to unix timestamp (in seconds)
+ **bucket**: Data is generally bucketed into hours or days
+ **metrics**: Comma separated list of metrics to include or that are included
+ **generated**: A unix timestamp (in seconds) when the data was generated to understand possibly stale data
+ **time**: A unix timestamp (in seconds)
+ **contributors_active**: number of unique social accounts with posts that have interactions
+ **contributors_created**: number of unique social accounts that created new posts
+ **interactions**: number of all publicly measurable interactions on a social post (views, likes, comments, thumbs up, upvote, share etc)
+ **posts_active**: number of unique social posts with interactions
+ **posts_created**: number of unique social posts created
+ **sentiment**: % of posts (weighted by interactions) that are positive. 100% means all posts are positive, 50% is half positive and half negative, and 0% is all negative posts.
+ **spam**: The number of posts created that are considered spam




---

### Category Posts

https://lunarcrush.com/api4/public/category/:category/posts/v1

Get the top posts for a social topic. If start time is provided the result will be the top posts by interactions for the time range. If start is not provided it will be the most recent top posts by interactions from the last 24 hours.

input parameters:

+ **category**: _Provide the category to get details for. A category must be all lower case and can only include letters, numbers, and spaces._ **required**
+ **start**: _The start time (unix timestamp) to start at. Will be rounded to the beginning of the day. If the end parameter is not provided it will just be the top posts for this day._ 
+ **end**: _(Optional) The end time (unix timestamp) to stop at. Will be rounded to the end of the day._ 

Example request:

```bash
curl -H "Authorization: Bearer <API_KEY>" https://lunarcrush.com/api4/public/category/cryptocurrencies/posts/v1
```



Example response:

```json
{
  "config": {
    "category": "cryptocurrencies",
    "type": "topic",
    "id": "_cryptocurrencies",
    "topic": "_cryptocurrencies",
    "generated": 1760647720
  },
  "data": [
    {
      "id": "t3_1o8b66k",
      "post_type": "reddit-post",
      "post_title": "Uptober",
      "post_link": "https://redd.it/1o8b66k",
      "post_image": null,
      "post_created": 1760645040,
      "post_sentiment": 3,
      "creator_id": "reddit::t2_123yyn",
      "creator_name": "skuntils",
      "creator_display_name": "skuntils",
      "creator_avatar": "https://styles.redditmedia.com/t5_ekeht/styles/profileIcon_snoof92c973c-0c87-4da9-a1cb-ee3475c3d920-headshot.png?width=256&height=256&crop=256:256,smart&s=33fc1ad631533a5b6ca1dc8ccff10621a3c3d103",
      "interactions_24h": 14135,
      "interactions_total": 14135
    }
  ]
}
```

Schema:

+ **config**: This includes the inputs for the request processed by the server and may include additional hints about the request and response information.
+ **category**: LunarCrush social category. Can only includes letters, numbers and spaces
+ **type**: Type of item or social network of item e.g. tweet, youtube-video, tiktok, x, youtube, category, topic, creator/influencer
+ **id**: Unique id of the social post
+ **topic**: LunarCrush social topic. Can only includes letters, numbers, spaces, #, and $
+ **generated**: A unix timestamp (in seconds) when the data was generated to understand possibly stale data
+ **post_type**: The type of social post
+ **post_title**: The title text of the social post
+ **post_link**: The URL to view the social post on the social network
+ **post_image**: The URL to the primary image for the post if available
+ **post_created**: The unix timestamp of our best indication of when the post was created
+ **post_sentiment**: The sentiment of the post is a score between 1 and 5 with 1 being very negative, 3 being neutral, and 5 being very positive. A score of 3.5 is considered slightly positive.
+ **creator_id**: The [network]::[unique_id] for the influencer
+ **creator_name**: The unique screen name for the influencer
+ **creator_display_name**: The chosen display name for the influencer if available
+ **creator_avatar**: The URL to the avatar for the creator
+ **interactions_24h**: Number of interactions in the last 24 hours
+ **interactions_total**: Number of total interactions




---

### Category News

https://lunarcrush.com/api4/public/category/:category/news/v1

Get the top news posts for a category. Top news is determined by the metrics related to the social posts that mention the news posts.

input parameters:

+ **category**: _Provide the category to get details for. A category must be all lower case and can only include letters, numbers, and spaces._ **required**

Example request:

```bash
curl -H "Authorization: Bearer <API_KEY>" https://lunarcrush.com/api4/public/category/cryptocurrencies/news/v1
```



Example response:

```json
{
  "config": {
    "category": "cryptocurrencies",
    "type": "topic",
    "id": "_cryptocurrencies",
    "topic": "_cryptocurrencies",
    "generated": 1760647721
  },
  "data": [
    {
      "id": "decrypt.co-460117231",
      "post_type": "news",
      "post_title": "Why Is Dogecoin Down So Much Worse Than Bitcoin and Ethereum? - Decrypt",
      "post_link": "https://decrypt.co/344674/why-dogecoin-down-worse-bitcoin-ethereum",
      "post_image": "https://cdn.decrypt.co/resize/1024/height/512/wp-content/uploads/2025/05/Doge4-gID_7.png",
      "post_created": 1760644348,
      "post_sentiment": 2.57,
      "creator_id": "twitter::993530753014054912",
      "creator_name": "DecryptMedia",
      "creator_display_name": "Decrypt",
      "creator_followers": 208065784,
      "creator_avatar": "https://pbs.twimg.com/profile_images/1864412071560892416/qTVkQadf_200x200.jpg",
      "interactions_24h": 1309,
      "interactions_total": 1521
    }
  ]
}
```

Schema:

+ **config**: This includes the inputs for the request processed by the server and may include additional hints about the request and response information.
+ **category**: LunarCrush social category. Can only includes letters, numbers and spaces
+ **type**: Type of item or social network of item e.g. tweet, youtube-video, tiktok, x, youtube, category, topic, creator/influencer
+ **id**: LunarCrush internal ID for the asset
+ **topic**: LunarCrush social topic. Can only includes letters, numbers, spaces, #, and $
+ **generated**: A unix timestamp (in seconds) when the data was generated to understand possibly stale data
+ **post_type**: The type of social post
+ **post_title**: The title text of the social post
+ **post_link**: The URL to view the social post on the social network
+ **post_image**: The URL to the primary image for the post if available
+ **post_created**: The unix timestamp of our best indication of when the post was created
+ **post_sentiment**: The sentiment of the post is a score between 1 and 5 with 1 being very negative, 3 being neutral, and 5 being very positive. A score of 3.5 is considered slightly positive.
+ **creator_id**: The [network]::[unique_id] for the influencer
+ **creator_name**: The unique screen name for the influencer
+ **creator_display_name**: The chosen display name for the influencer if available
+ **creator_followers**: number of followers the account has
+ **creator_avatar**: The URL to the avatar for the creator
+ **interactions_24h**: Number of interactions in the last 24 hours
+ **interactions_total**: Number of total interactions




---

### Category Creators

https://lunarcrush.com/api4/public/category/:category/creators/v1

Get the top creators for a social category

input parameters:

+ **category**: _Provide the category to get details for. A category must be all lower case and can only include letters, numbers, and spaces._ **required**

Example request:

```bash
curl -H "Authorization: Bearer <API_KEY>" https://lunarcrush.com/api4/public/category/musicians/creators/v1
```



Example response:

```json
{
  "data": [
    {
      "creator_id": "twitter::79293791",
      "creator_name": "rihanna",
      "creator_avatar": "https://pbs.twimg.com/profile_images/1960786225423659008/GhLekHuP_200x200.jpg",
      "creator_followers": 106933122,
      "creator_rank": 1,
      "interactions_24h": 21430912
    }
  ]
}
```

Schema:

+ **creator_id**: The [network]::[unique_id] for the influencer
+ **creator_name**: The unique screen name for the influencer
+ **creator_avatar**: The URL to the avatar for the creator
+ **creator_followers**: number of followers the account has
+ **creator_rank**: ranking based on all posts in the last 24 hours that have interactions
+ **interactions_24h**: Number of interactions in the last 24 hours




---

### Categories List

https://lunarcrush.com/api4/public/categories/list/v1

Get a list of trending social categories.

Example request:

```bash
curl -H "Authorization: Bearer <API_KEY>" https://lunarcrush.com/api4/public/categories/list/v1
```



Example response:

```json
{
  "data": [
    {
      "category": "la liga",
      "title": "La Liga",
      "category_rank": 19,
      "category_rank_1h_previous": 19,
      "category_rank_24h_previous": 21,
      "num_contributors": 13509,
      "social_dominance": 0.2997582337382281,
      "num_posts": 23407,
      "interactions_24h": 111594557
    }
  ]
}
```

Schema:

+ **category**: LunarCrush social category. Can only includes letters, numbers and spaces
+ **title**: The case sensitive title of the topic or category
+ **category_rank**: LunarCrush metric for ranking a social topic relative to all other social topics
+ **category_rank_1h_previous**: The topic rank from 1 hour ago
+ **category_rank_24h_previous**: The topic rank from 24 hours ago
+ **num_contributors**: The number of unique social contributors to the topic
+ **social_dominance**: The percent of the total social volume that this topic represents
+ **num_posts**: Total number of posts with interactions on this topic in the last 24 hours
+ **interactions_24h**: Number of interactions in the last 24 hours




---

### Creators List

https://lunarcrush.com/api4/public/creators/list/v1

Get a list of trending social creators over all of social based on interactions. To get lists of creators by category or topic see the topics and categories endpoints.

Example request:

```bash
curl -H "Authorization: Bearer <API_KEY>" https://lunarcrush.com/api4/public/creators/list/v1
```



Example response:

```json
{
  "data": [
    {
      "creator_name": "FoxNews",
      "creator_display_name": "Fox News",
      "creator_id": "1367531",
      "creator_network": "twitter",
      "creator_avatar": "https://pbs.twimg.com/profile_images/1956414642370015232/GEq5Z9jN_200x200.png",
      "creator_followers": 208065784,
      "creator_posts": 2299,
      "creator_rank": 1,
      "interactions_24h": 334657566
    }
  ]
}
```

Schema:

+ **creator_name**: The unique screen name for the influencer
+ **creator_display_name**: The chosen display name for the influencer if available
+ **creator_id**: The [network]::[unique_id] for the influencer
+ **creator_network**: The social network for the post or influencer. We still refer to x as twitter out of developer preference.
+ **creator_avatar**: The URL to the avatar for the creator
+ **creator_followers**: number of followers the account has
+ **creator_posts**: total number of posts with interactions in the last 24 hours
+ **creator_rank**: ranking based on all posts in the last 24 hours that have interactions
+ **interactions_24h**: Number of interactions in the last 24 hours




---

### Creator

https://lunarcrush.com/api4/public/creator/:network/:id/v1

Get detail information on a specific creator

input parameters:

+ **network**: _Provide the network for the creator. One of twitter, youtube, instagram, reddit, or tiktok_ **required**
+ **id**: _Provide the unique ID or screen name of the creator_ **required**

Example request:

```bash
curl -H "Authorization: Bearer <API_KEY>" https://lunarcrush.com/api4/public/creator/twitter/elonmusk/v1
```



Example response:

```json
{
  "data": {
    "creator_id": "twitter::44196397",
    "creator_name": "elonmusk",
    "creator_display_name": "Elon Musk",
    "creator_avatar": "https://pbs.twimg.com/profile_images/1936002956333080576/kqqe2iWO_200x200.jpg",
    "creator_followers": 227854844,
    "creator_rank": 4,
    "interactions_24h": 120031096,
    "topic_influence": [
      {
        "topic": "elon musk",
        "count": 189,
        "percent": 1.71,
        "rank": 1
      }
    ],
    "top_community": [
      {
        "creator_name": "grok",
        "creator_display_name": "Grok",
        "creator_avatar": "https://pbs.twimg.com/profile_images/1893219113717342208/Vgg2hEPa_200x200.jpg",
        "count": 343
      }
    ]
  }
}
```

Schema:

+ **creator_id**: The [network]::[unique_id] for the influencer
+ **creator_name**: The unique screen name for the influencer
+ **creator_display_name**: The chosen display name for the influencer if available
+ **creator_avatar**: The URL to the avatar for the creator
+ **creator_followers**: number of followers the account has
+ **creator_rank**: ranking based on all posts in the last 24 hours that have interactions
+ **interactions_24h**: Number of interactions in the last 24 hours
+ **topic_influence**: an array of social topics and the creators ranking on each topic
+ **topic**: LunarCrush social topic. Can only includes letters, numbers, spaces, #, and $
+ **top_community**: an array of the top accounts that have recently mentioned this creator or that this creator has mentioned




---

### Creator Time Series

https://lunarcrush.com/api4/public/creator/:network/:id/time-series/v1

Get time series data on a creator.

input parameters:

+ **network**: _Influencer social network_ **required**
+ **id**: _The unique id or screen name of the creator_ **required**
+ **bucket**: _bucket time series data into hours or days. default is hours._ 
+ **interval**: _Use interval to specify the start and end time automatically for convenience. If "start" or "end" parameters are provided this parameter is ignored._ 
+ **start**: _The start time (unix timestamp) to go back to._ 
+ **end**: _The end time (unix timestamp) to stop at._ 

Example request:

```bash
curl -H "Authorization: Bearer <API_KEY>" https://lunarcrush.com/api4/public/creator/twitter/lunarcrush/time-series/v1
```



Example response:

```json
{
  "config": {
    "network": "twitter",
    "influencer_id": "twitter::988992203568562176",
    "interval": "1w",
    "start": 1759968000,
    "end": 1760659200,
    "bucket": "hour",
    "name": "lunarcrush",
    "remote_api": "danode1-13",
    "generated": 1760647721
  },
  "data": [
    {
      "time": 1759968000,
      "followers": 309011,
      "interactions": 6824,
      "posts_active": 35,
      "creator_rank": 274812
    }
  ]
}
```

Schema:

+ **config**: This includes the inputs for the request processed by the server and may include additional hints about the request and response information.
+ **network**: The social network for the post or influencer. We still refer to x as twitter out of developer preference.
+ **interval**: Typically used for specifying time intervals like 1w = 1 week, 1m = 1 month etc
+ **start**: Start/from unix timestamp (in seconds)
+ **end**: End/to unix timestamp (in seconds)
+ **bucket**: Data is generally bucketed into hours or days
+ **name**: The full name of the asset
+ **generated**: A unix timestamp (in seconds) when the data was generated to understand possibly stale data
+ **time**: A unix timestamp (in seconds)
+ **followers**: The number of publicly displayed followers the creator has
+ **interactions**: number of all publicly measurable interactions on a social post (views, likes, comments, thumbs up, upvote, share etc)
+ **posts_active**: number of unique social posts with interactions
+ **creator_rank**: ranking based on all posts in the last 24 hours that have interactions




---

### Creator Posts

https://lunarcrush.com/api4/public/creator/:network/:id/posts/v1

Get the top posts for a specific creator. If start time is provided the result will be the top posts by interactions for the time range. If start is not provided it will be the most recent top posts by interactions from the last 24 hours.

input parameters:

+ **network**: _Network for the creator. One of twitter, youtube, instagram, reddit, or tiktok_ **required**
+ **id**: _Unique ID or screen name of the creator_ **required**
+ **start**: _The start time (unix timestamp) to start at. Will be rounded to the beginning of the day. If the end parameter is not provided it will just be the top posts for this day._ 
+ **end**: _(Optional) The end time (unix timestamp) to stop at. Will be rounded to the end of the day._ 

Example request:

```bash
curl -H "Authorization: Bearer <API_KEY>" https://lunarcrush.com/api4/public/creator/twitter/elonmusk/posts/v1
```



Example response:

```json
{
  "data": [
    {
      "id": "1953886838445552084",
      "post_type": "tweet",
      "post_title": "Good idea. \n\nAlso, we will be putting the most liked images on ð• in the Grok Imagine default feed.",
      "post_created": 1754677898,
      "post_sentiment": 3.48,
      "post_link": "https://x.com/elonmusk/status/1953886838445552084",
      "post_image": null,
      "creator_id": "twitter::44196397",
      "creator_name": "elonmusk",
      "creator_display_name": "Elon Musk",
      "creator_followers": 227846462,
      "creator_avatar": "https://pbs.twimg.com/profile_images/1936002956333080576/kqqe2iWO_200x200.jpg",
      "interactions_24h": 0,
      "interactions_total": 18444057
    }
  ]
}
```

Schema:

+ **id**: Unique id of the social post
+ **post_type**: The type of social post
+ **post_title**: The title text of the social post
+ **post_created**: The unix timestamp of our best indication of when the post was created
+ **post_sentiment**: The sentiment of the post is a score between 1 and 5 with 1 being very negative, 3 being neutral, and 5 being very positive. A score of 3.5 is considered slightly positive.
+ **post_link**: The URL to view the social post on the social network
+ **post_image**: The URL to the primary image for the post if available
+ **creator_id**: The [network]::[unique_id] for the influencer
+ **creator_name**: The unique screen name for the influencer
+ **creator_display_name**: The chosen display name for the influencer if available
+ **creator_followers**: number of followers the account has
+ **creator_avatar**: The URL to the avatar for the creator
+ **interactions_24h**: Number of interactions in the last 24 hours
+ **interactions_total**: Number of total interactions




---

### Posts

https://lunarcrush.com/api4/public/posts/:post_type/:post_id/v1

Get details of a post

input parameters:

+ **post_type**: _The post type e.g. tweet, youtube-video, tiktok-video, reddit-post, instagram-post_ **required**
+ **post_id**: _The unique id of a post, for twitter it is a number, youtube it is the id in the url after watch?v=, look in the url for the unique id_ **required**

Example request:

```bash
curl -H "Authorization: Bearer <API_KEY>" https://lunarcrush.com/api4/public/posts/tweet/1756378079893782591/v1
```



Example response:

```json
{
  "type": "tweet",
  "id": "1756378079893782591",
  "title": "Social activity is ðŸ‘† across the board today. \n\nðŸ¤” What are y'all talking about? \nðŸ«¡ We've got you covered.\n\nðŸ‘©â€ðŸ’» Technology\nðŸ’¬ Social Networks\nðŸ‘¨â€ðŸŽ¤ Musicians\nðŸ•º Celebrities\nðŸŒ Countries\nðŸŽ® Gaming\nðŸ–ï¸ Travel\nðŸš— Automotive\nðŸ¥· Cryptocurrencies\nðŸ‡ºðŸ‡¸ US Election\n\nðŸš€ https://t.co/AI5yuZEyi7 https://t.co/T0mqJBiyx0",
  "description": null,
  "extraText": "https://lunarcrush.com/categories?rpp=300&page=1&cols=topic_rank%2Ccontributors_active%2Cposts_active%2Caverage_sentiment%2Cinteractions_24h%2Cinteractions_trend",
  "metrics": {
    "bookmarks": 1,
    "favorites": 20,
    "retweets": 3,
    "replies": 13,
    "views": 13005
  },
  "image": {
    "src": "https://pbs.twimg.com/media/GF_n3GQaoAA23sT.jpg",
    "width": 2048,
    "height": 989
  },
  "video": null,
  "images": null,
  "creator_id": "twitter::988992203568562176",
  "creator_name": "LunarCrush",
  "creator_display_name": "LunarCrush Social Analytics",
  "creator_avatar": "https://pbs.twimg.com/profile_images/1958717678476304384/CbzjwJvB_200x200.png",
  "topics": [
    "social networks"
  ],
  "categories": []
}
```

Schema:

+ **type**: Type of item or social network of item e.g. tweet, youtube-video, tiktok, x, youtube, category, topic, creator/influencer
+ **id**: Unique id of the social post
+ **title**: Title of the social post
+ **description**: Explanation of the change and the potential impact
+ **extraText**: Extra text for the post for search matching like the retweet text or text included in the video
+ **metrics**: Comma separated list of metrics to include or that are included
+ **image**: Provides the url/src width and height of a the image in the post if available
+ **video**: Provides the url/src width and height of a the video in the post if available
+ **images**: Provides the url/src width and height of a the images in the post if available
+ **creator_id**: The [network]::[unique_id] for the influencer
+ **creator_name**: The unique screen name for the influencer
+ **creator_display_name**: The chosen display name for the influencer if available
+ **creator_avatar**: The URL to the avatar for the creator
+ **categories**: an array of categories this topic aggregates into




---

### Posts Time Series

https://lunarcrush.com/api4/public/posts/:post_type/:post_id/time-series/v1

Get interactions over time for a post. If a post is older than 365 days the time series will be returned as daily interactions, otherwise it hourly interactions

input parameters:

+ **post_type**: _The post type e.g. tweet, youtube-video, tiktok-video, reddit-post, instagram-post_ **required**
+ **post_id**: _The unique id of a post, for twitter it is a number, youtube it is the id in the url after watch?v=, look in the url for the unique id_ **required**

Example request:

```bash
curl -H "Authorization: Bearer <API_KEY>" https://lunarcrush.com/api4/public/posts/tweet/1756378079893782591/time-series/v1
```



Example response:

```json
{
  "data": [
    {
      "time": "1707523200",
      "interactions": 24
    }
  ]
}
```

Schema:

+ **time**: A unix timestamp (in seconds)
+ **interactions**: number of all publicly measurable interactions on a social post (views, likes, comments, thumbs up, upvote, share etc)




---

### Coins List v2

https://lunarcrush.com/api4/public/coins/list/v2

Get a general snapshot of LunarCrush metrics on the entire list of tracked coins. It is designed as a lightweight mechanism for monitoring the universe of available assets, either in aggregate or relative to each other. Metrics include Galaxy Scoreâ„¢, AltRankâ„¢, price, volatility, 24h percent change, market cap, social mentions, social interactions, social contributors, social dominance, and categories.

input parameters:

+ **sort**: _sort the output by metric_ 
+ **filter**: _filter by sub categories / sector from the "categories" key. Separate by commas for multiple matches. Available sectors can be found on the sector filters at https://lunarcrush.com/categories/cryptocurrencies_ 
+ **limit**: _limit the number of results. Default is 10 maximum is 1000 per page._ 
+ **desc**: _Pass any value as desc and the output will be reversed (descending)_ 
+ **page**: _When using limit, set the page of results to display, pages start at 0_ 

Example request:

```bash
curl -H "Authorization: Bearer <API_KEY>" https://lunarcrush.com/api4/public/coins/list/v2
```



Example response:

```json
{
  "config": {
    "sort": "market_cap_rank",
    "desc": true,
    "limit": 0,
    "page": 0,
    "total_rows": 7515,
    "generated": 1760647722
  },
  "data": [
    {
      "id": 1,
      "symbol": "BTC",
      "name": "Bitcoin",
      "price": 108017.15003117608,
      "price_btc": 1,
      "volume_24h": 87883021801.69,
      "volatility": 0.012,
      "circulating_supply": 19934406,
      "max_supply": 21000000,
      "percent_change_1h": -0.014473410106,
      "percent_change_24h": -2.854897331006,
      "percent_change_7d": -10.825609124776,
      "market_cap": 2153257723684.38,
      "market_cap_rank": 1,
      "interactions_24h": 183243410,
      "social_volume_24h": 353615,
      "social_dominance": 35.51064470777264,
      "market_dominance": 58.726273413735896,
      "market_dominance_prev": 57.17439621343422,
      "galaxy_score": 40.5,
      "galaxy_score_previous": 43,
      "alt_rank": 321,
      "alt_rank_previous": 184,
      "sentiment": 75,
      "categories": "layer-1,bitcoin-ecosystem,pow",
      "blockchains": [
        {
          "type": "layer1",
          "network": "bitcoin",
          "address": null,
          "decimals": null
        }
      ],
      "percent_change_30d": -7.605660649422,
      "last_updated_price": 1760647713,
      "last_updated_price_by": "cmc_stream",
      "topic": "btc bitcoin",
      "logo": "https://cdn.lunarcrush.com/bitcoin.png"
    }
  ]
}
```

Schema:

+ **config**: This includes the inputs for the request processed by the server and may include additional hints about the request and response information.
+ **generated**: A unix timestamp (in seconds) when the data was generated to understand possibly stale data
+ **id**: LunarCrush internal ID for the asset
+ **symbol**: The symbol for the asset
+ **name**: The full name of the asset
+ **price**: Current price in USD
+ **price_btc**: Current price in BTC
+ **volume_24h**: Volume in USD for 24 hours up to this data point
+ **volatility**: Volatility is calculated as the standard deviation of the price.
+ **circulating_supply**: Circulating Supply is the total number of coins or tokens that are actively available for trade and are being used in the market and in general public
+ **max_supply**: The maximum supply of the asset if available
+ **percent_change_1h**: Percent change in price since 1 hour ago
+ **percent_change_24h**: Percent change in price since 24 hours ago
+ **percent_change_7d**: Percent change in price since 7 days ago
+ **market_cap**: Total dollar market value of all circulating supply or outstanding shares
+ **market_cap_rank**: The rank of the asset by market cap with additional filtering to remove outliers and bad market data.
+ **interactions_24h**: Number of interactions in the last 24 hours
+ **social_volume_24h**: Total number of posts with interactions on this topic in the last 24 hours
+ **social_dominance**: The percent of the total social volume that this topic represents
+ **market_dominance**: The percent of the total market cap that this asset represents
+ **galaxy_score**: A proprietary score based on technical indicators of price, average social sentiment, relative social activity, and a factor of how closely social indicators correlate with price and volume
+ **galaxy_score_previous**: The galaxy score from the previous 24 hours
+ **alt_rank**: A proprietary score based on how an asset is performing relative to all other assets supported
+ **alt_rank_previous**: The alt rank from the previous 24 hours
+ **sentiment**: % of posts (weighted by interactions) that are positive. 100% means all posts are positive, 50% is half positive and half negative, and 0% is all negative posts.
+ **categories**: A comma delimited string of sub categories/sectors this asset belongs to
+ **blockchains**: An array of blockchains that the asset is part of including the contract address and decimals if applicable
+ **type**: Type of item or social network of item e.g. tweet, youtube-video, tiktok, x, youtube, category, topic, creator/influencer
+ **network**: The name of the blockchain or network
+ **address**: The contract address, zero or null means it is a layer 1
+ **percent_change_30d**: Percent change in price since 30 days ago
+ **topic**: LunarCrush social topic. Can only includes letters, numbers, spaces, #, and $
+ **logo**: The URL to the logo for the asset, topic, or category




---

### Coins List

https://lunarcrush.com/api4/public/coins/list/v1

Get a general snapshot of LunarCrush metrics on the entire list of tracked coins. This version is heavily cached and up to 1 hour behind. It is designed as a lightweight mechanism for monitoring the universe of available assets, either in aggregate or relative to each other. Metrics include Galaxy Scoreâ„¢, AltRankâ„¢, price, volatility, 24h percent change, market cap, social mentions, social interactions, social contributors, social dominance, and categories. Use the coins/list/v2 endpoint for data updated every few seconds.

input parameters:

+ **sort**: _sort the output by metric_ 
+ **filter**: _filter by sub categories / sector from the "categories" key. Separate by commas for multiple matches. Available sectors can be found on the sector filters at https://lunarcrush.com/categories/cryptocurrencies_ 
+ **limit**: _limit the number of results. Default is 10 maximum is 1000 per page._ 
+ **desc**: _Pass any value as desc and the output will be reversed (descending)_ 
+ **page**: _When using limit, set the page of results to display, pages start at 0_ 

Example request:

```bash
curl -H "Authorization: Bearer <API_KEY>" https://lunarcrush.com/api4/public/coins/list/v1
```



Example response:

```json
{
  "config": {
    "sort": "market_cap_rank",
    "desc": true,
    "limit": 0,
    "page": 0,
    "total_rows": 7515,
    "generated": 1760647722
  },
  "data": [
    {
      "id": 1,
      "symbol": "BTC",
      "name": "Bitcoin",
      "price": 108017.15003117608,
      "price_btc": 1,
      "volume_24h": 87883021801.69,
      "volatility": 0.012,
      "circulating_supply": 19934406,
      "max_supply": 21000000,
      "percent_change_1h": -0.014473410106,
      "percent_change_24h": -2.854897331006,
      "percent_change_7d": -10.825609124776,
      "market_cap": 2153257723684.38,
      "market_cap_rank": 1,
      "interactions_24h": 183243410,
      "social_volume_24h": 353615,
      "social_dominance": 35.51064470777264,
      "market_dominance": 58.726273413735896,
      "market_dominance_prev": 57.17439621343422,
      "galaxy_score": 40.5,
      "galaxy_score_previous": 43,
      "alt_rank": 321,
      "alt_rank_previous": 184,
      "sentiment": 75,
      "categories": "layer-1,bitcoin-ecosystem,pow",
      "blockchains": [
        {
          "type": "layer1",
          "network": "bitcoin",
          "address": null,
          "decimals": null
        }
      ],
      "percent_change_30d": -7.605660649422,
      "last_updated_price": 1760647713,
      "last_updated_price_by": "cmc_stream",
      "topic": "btc bitcoin",
      "logo": "https://cdn.lunarcrush.com/bitcoin.png"
    }
  ]
}
```

Schema:

+ **config**: This includes the inputs for the request processed by the server and may include additional hints about the request and response information.
+ **generated**: A unix timestamp (in seconds) when the data was generated to understand possibly stale data
+ **id**: LunarCrush internal ID for the asset
+ **symbol**: The symbol for the asset
+ **name**: The full name of the asset
+ **price**: Current price in USD
+ **price_btc**: Current price in BTC
+ **volume_24h**: Volume in USD for 24 hours up to this data point
+ **volatility**: Volatility is calculated as the standard deviation of the price.
+ **circulating_supply**: Circulating Supply is the total number of coins or tokens that are actively available for trade and are being used in the market and in general public
+ **max_supply**: The maximum supply of the asset if available
+ **percent_change_1h**: Percent change in price since 1 hour ago
+ **percent_change_24h**: Percent change in price since 24 hours ago
+ **percent_change_7d**: Percent change in price since 7 days ago
+ **market_cap**: Total dollar market value of all circulating supply or outstanding shares
+ **market_cap_rank**: The rank of the asset by market cap with additional filtering to remove outliers and bad market data.
+ **interactions_24h**: Number of interactions in the last 24 hours
+ **social_volume_24h**: Total number of posts with interactions on this topic in the last 24 hours
+ **social_dominance**: The percent of the total social volume that this topic represents
+ **market_dominance**: The percent of the total market cap that this asset represents
+ **galaxy_score**: A proprietary score based on technical indicators of price, average social sentiment, relative social activity, and a factor of how closely social indicators correlate with price and volume
+ **galaxy_score_previous**: The galaxy score from the previous 24 hours
+ **alt_rank**: A proprietary score based on how an asset is performing relative to all other assets supported
+ **alt_rank_previous**: The alt rank from the previous 24 hours
+ **sentiment**: % of posts (weighted by interactions) that are positive. 100% means all posts are positive, 50% is half positive and half negative, and 0% is all negative posts.
+ **categories**: A comma delimited string of sub categories/sectors this asset belongs to
+ **blockchains**: An array of blockchains that the asset is part of including the contract address and decimals if applicable
+ **type**: Type of item or social network of item e.g. tweet, youtube-video, tiktok, x, youtube, category, topic, creator/influencer
+ **network**: The name of the blockchain or network
+ **address**: The contract address, zero or null means it is a layer 1
+ **percent_change_30d**: Percent change in price since 30 days ago
+ **topic**: LunarCrush social topic. Can only includes letters, numbers, spaces, #, and $
+ **logo**: The URL to the logo for the asset, topic, or category




---

### Coins

https://lunarcrush.com/api4/public/coins/:coin/v1

Get market data on a coin or token. Specify the coin to be queried by providing the numeric ID or the symbol of the coin in the input parameter, which can be found by calling the /coins/list endpoint.

input parameters:

+ **coin**: _provide the numeric id or symbol of the coin or token._ **required**

Example request:

```bash
curl -H "Authorization: Bearer <API_KEY>" https://lunarcrush.com/api4/public/coins/2/v1
```



Example response:

```json
{
  "config": {
    "id": "coins:2",
    "name": "Ethereum",
    "symbol": "ETH",
    "topic": "ethereum",
    "generated": 1760647723
  },
  "data": {
    "id": 2,
    "name": "Ethereum",
    "symbol": "ETH",
    "price": 3862.216744258913,
    "price_btc": 0.0357663915983591,
    "market_cap": 466164873671.08,
    "percent_change_24h": -2.73840704595,
    "percent_change_7d": -11.09102922116,
    "percent_change_30d": -14.136006116255,
    "volume_24h": 48782186383.58,
    "max_supply": null,
    "circulating_supply": 120698786.35,
    "close": 3862.216744258913,
    "galaxy_score": 53.6,
    "alt_rank": 339,
    "volatility": 0.0191,
    "market_cap_rank": 2
  }
}
```

Schema:

+ **config**: This includes the inputs for the request processed by the server and may include additional hints about the request and response information.
+ **id**: LunarCrush internal ID for the asset
+ **name**: The full name of the asset
+ **symbol**: The symbol for the asset
+ **topic**: LunarCrush social topic. Can only includes letters, numbers, spaces, #, and $
+ **generated**: A unix timestamp (in seconds) when the data was generated to understand possibly stale data
+ **price**: Current price in USD
+ **price_btc**: Current price in BTC
+ **market_cap**: Total dollar market value of all circulating supply or outstanding shares
+ **percent_change_24h**: Percent change in price since 24 hours ago
+ **percent_change_7d**: Percent change in price since 7 days ago
+ **percent_change_30d**: Percent change in price since 30 days ago
+ **volume_24h**: Volume in USD for 24 hours up to this data point
+ **max_supply**: The maximum supply of the asset if available
+ **circulating_supply**: Circulating Supply is the total number of coins or tokens that are actively available for trade and are being used in the market and in general public
+ **close**: Close price for the time period
+ **galaxy_score**: A proprietary score based on technical indicators of price, average social sentiment, relative social activity, and a factor of how closely social indicators correlate with price and volume
+ **alt_rank**: A proprietary score based on how an asset is performing relative to all other assets supported
+ **volatility**: Volatility is calculated as the standard deviation of the price.
+ **market_cap_rank**: The rank of the asset by market cap with additional filtering to remove outliers and bad market data.




---

### Coins Time Series

https://lunarcrush.com/api4/public/coins/:coin/time-series/v2

Get market time series data on a coin or token. Specify the coin to be queried by providing the numeric ID or the symbol of the coin in the input parameter, which can be found by calling the /coins/list endpoint.

input parameters:

+ **coin**: _provide the numeric id or symbol of the coin or token._ **required**
+ **bucket**: _bucket time series data into hours or days. default is hours._ 
+ **interval**: _Use interval to specify the start and end time automatically for convenience. If "start" or "end" parameters are provided this parameter is ignored._ 
+ **start**: _The start time (unix timestamp) to go back to._ 
+ **end**: _The end time (unix timestamp) to stop at._ 

Example request:

```bash
curl -H "Authorization: Bearer <API_KEY>" https://lunarcrush.com/api4/public/coins/2/time-series/v2
```



Example response:

```json
{
  "config": {
    "coin": "2",
    "topic": "ethereum",
    "id": "coins:2",
    "name": "Ethereum",
    "symbol": "ETH",
    "interval": "1w",
    "start": 1759968000,
    "end": 1760654923,
    "bucket": "hour",
    "metrics": [],
    "generated": 1760647723
  },
  "data": [
    {
      "time": 1759968000,
      "contributors_active": 11287,
      "contributors_created": 458,
      "interactions": 1119245,
      "posts_active": 19827,
      "posts_created": 659,
      "sentiment": 82,
      "spam": 263,
      "alt_rank": 192,
      "circulating_supply": 120702112,
      "close": 4516.9,
      "galaxy_score": 49,
      "high": 4516.9,
      "low": 4513.99,
      "market_cap": 545595967799,
      "market_dominance": 12.9078,
      "open": 4516.9,
      "social_dominance": 9.5436,
      "volume_24h": 39542478282
    }
  ]
}
```

Schema:

+ **config**: This includes the inputs for the request processed by the server and may include additional hints about the request and response information.
+ **topic**: LunarCrush social topic. Can only includes letters, numbers, spaces, #, and $
+ **id**: LunarCrush internal ID for the asset
+ **name**: The full name of the asset
+ **symbol**: The symbol for the asset
+ **interval**: Typically used for specifying time intervals like 1w = 1 week, 1m = 1 month etc
+ **start**: Start/from unix timestamp (in seconds)
+ **end**: End/to unix timestamp (in seconds)
+ **bucket**: Data is generally bucketed into hours or days
+ **metrics**: Comma separated list of metrics to include or that are included
+ **generated**: A unix timestamp (in seconds) when the data was generated to understand possibly stale data
+ **time**: A unix timestamp (in seconds)
+ **contributors_active**: number of unique social accounts with posts that have interactions
+ **contributors_created**: number of unique social accounts that created new posts
+ **interactions**: number of all publicly measurable interactions on a social post (views, likes, comments, thumbs up, upvote, share etc)
+ **posts_active**: number of unique social posts with interactions
+ **posts_created**: number of unique social posts created
+ **sentiment**: % of posts (weighted by interactions) that are positive. 100% means all posts are positive, 50% is half positive and half negative, and 0% is all negative posts.
+ **spam**: The number of posts created that are considered spam
+ **alt_rank**: A proprietary score based on how an asset is performing relative to all other assets supported
+ **circulating_supply**: Circulating Supply is the total number of coins or tokens that are actively available for trade and are being used in the market and in general public
+ **close**: Close price for the time period
+ **galaxy_score**: A proprietary score based on technical indicators of price, average social sentiment, relative social activity, and a factor of how closely social indicators correlate with price and volume
+ **high**: Higest price fo rthe time period
+ **low**: Lowest price for the time period
+ **market_cap**: Total dollar market value of all circulating supply or outstanding shares
+ **market_dominance**: The percent of the total market cap that this asset represents
+ **open**: Open price for the time period
+ **social_dominance**: The percent of the total social volume that this topic represents
+ **volume_24h**: Volume in USD for 24 hours up to this data point




---

### Coins Meta

https://lunarcrush.com/api4/public/coins/:coin/meta/v1

Get meta information for a cryptocurrency project. This includes information such as the website, social media links, and other information.

input parameters:

+ **coin**: _provide the numeric id or symbol of the coin or token._ **required**

Example request:

```bash
curl -H "Authorization: Bearer <API_KEY>" https://lunarcrush.com/api4/public/coins/2/meta/v1
```



Example response:

```json
{
  "data": {
    "id": 2,
    "name": "Ethereum",
    "symbol": "ETH",
    "market_categories": "layer-1",
    "updated": 1741059248,
    "blockchain": [
      {
        "type": "layer1",
        "network": "ethereum",
        "address": null,
        "decimals": null
      }
    ],
    "short_summary": "Ethereum is open access to digital money and data-friendly services for everyone â€“ no matter your background or location. It's a community-built technology behind the cryptocurrency ether (ETH) and thousands of applications you can use today.",
    "description": "Ethereum is a technology that lets you send cryptocurrency to anyone for a small fee. It also powers applications that everyone can use and no one can take down.\n\nIt's the world's programmable blockchain.\n\nEthereum builds on Bitcoin's innovation, with some big differences.\n\nBoth let you use digital money without payment providers or banks. But Ethereum is programmable, so you can also use it for lots of different digital assets â€“ even Bitcoin!\n\nThis also means Ethereum is for more than payments. It's a marketplace of financial services, games and apps that can't steal your data or censor you.",
    "github_link": "https://github.com/ethereum",
    "website_link": "https://www.ethereum.org/",
    "whitepaper_link": "https://ethereum.org/en/whitepaper",
    "twitter_link": "https://twitter.com/ethereum",
    "reddit_link": "https://www.reddit.com/r/ethereum/",
    "header_image": "headers/ethereum.png",
    "header_text": "The foundation for our digital future",
    "videos": "https://www.youtube.com/watch?v=GQR1xjQn5Pg",
    "coingecko_link": "https://www.coingecko.com/en/coins/ethereum",
    "coinmarketcap_link": "https://coinmarketcap.com/currencies/ethereum/"
  },
  "config": {
    "coin": "2",
    "generated": 1760647723
  }
}
```

Schema:

+ **id**: LunarCrush internal ID for the asset
+ **name**: The full name of the asset
+ **symbol**: The symbol for the asset
+ **updated**: Timestamp of when the data was last updated
+ **type**: Type of item or social network of item e.g. tweet, youtube-video, tiktok, x, youtube, category, topic, creator/influencer
+ **network**: The social network for the post or influencer. We still refer to x as twitter out of developer preference.
+ **description**: Explanation of the change and the potential impact
+ **config**: This includes the inputs for the request processed by the server and may include additional hints about the request and response information.
+ **generated**: A unix timestamp (in seconds) when the data was generated to understand possibly stale data




---

### Stocks List v2

https://lunarcrush.com/api4/public/stocks/list/v2

Get a general snapshot of LunarCrush metrics on the entire list of tracked stocks. It is designed as a lightweight mechanism for monitoring the universe of available assets, either in aggregate or relative to each other. Metrics include Galaxy Scoreâ„¢, AltRankâ„¢, floor price, 24h percent change, market cap, social mentions, social interactions, social contributors, social dominance, and categories.

input parameters:

+ **sort**: _sort the output by metric_ 
+ **limit**: _limit the number of results. Default is 10 maximum is 100 per page._ 
+ **desc**: _Pass any value as desc and the output will be reversed (descending)_ 
+ **page**: _When using limit, set the page of results to display, pages start at 0_ 

Example request:

```bash
curl -H "Authorization: Bearer <API_KEY>" https://lunarcrush.com/api4/public/stocks/list/v2
```



Example response:

```json
{
  "config": {
    "limit": 0,
    "sort": "market_cap_rank",
    "desc": true,
    "page": 0,
    "total_rows": 2270,
    "generated": 1760647723
  },
  "data": [
    {
      "id": 52199,
      "symbol": "TSM",
      "name": "Taiwan Semiconductor",
      "price": 299.84,
      "volume_24h": 21050629762.120003,
      "percent_change_24h": -1.6277772308096154,
      "market_cap": 1555127087503.36,
      "market_cap_rank": 1,
      "interactions_24h": 6003306,
      "social_volume_24h": 7254,
      "social_dominance": 0.8887364236138763,
      "market_dominance": 1.862154878310016,
      "market_dominance_prev": 1.960328599836193,
      "galaxy_score": 52.3,
      "galaxy_score_previous": 52,
      "alt_rank": 665,
      "alt_rank_previous": 195,
      "sentiment": 81,
      "categories": "technology",
      "last_updated_price": 1760647688,
      "last_updated_price_by": "polygon_market",
      "topic": "tsm taiwan semiconductor",
      "logo": "https://cdn.lunarcrush.com/stocks/tsm.png"
    }
  ]
}
```

Schema:

+ **config**: This includes the inputs for the request processed by the server and may include additional hints about the request and response information.
+ **generated**: A unix timestamp (in seconds) when the data was generated to understand possibly stale data
+ **id**: LunarCrush internal ID for the asset
+ **symbol**: The symbol for the asset
+ **name**: The full name of the asset
+ **price**: Current price in USD
+ **volume_24h**: Volume in USD for 24 hours up to this data point
+ **percent_change_24h**: Percent change in price since 24 hours ago
+ **market_cap**: Total dollar market value of all circulating supply or outstanding shares
+ **market_cap_rank**: The rank of the asset by market cap with additional filtering to remove outliers and bad market data.
+ **interactions_24h**: Number of interactions in the last 24 hours
+ **social_volume_24h**: Total number of posts with interactions on this topic in the last 24 hours
+ **social_dominance**: The percent of the total social volume that this topic represents
+ **market_dominance**: The percent of the total market cap that this asset represents
+ **galaxy_score**: A proprietary score based on technical indicators of price, average social sentiment, relative social activity, and a factor of how closely social indicators correlate with price and volume
+ **galaxy_score_previous**: The galaxy score from the previous 24 hours
+ **alt_rank**: A proprietary score based on how an asset is performing relative to all other assets supported
+ **alt_rank_previous**: The alt rank from the previous 24 hours
+ **sentiment**: % of posts (weighted by interactions) that are positive. 100% means all posts are positive, 50% is half positive and half negative, and 0% is all negative posts.
+ **categories**: an array of categories this topic aggregates into
+ **topic**: LunarCrush social topic. Can only includes letters, numbers, spaces, #, and $
+ **logo**: The URL to the logo for the asset, topic, or category




---

### Stocks List

https://lunarcrush.com/api4/public/stocks/list/v1

Lists all stocks supported by LunarCrush. Includes the "topic" endpoint to use to get social data from this asset as a social topic.

input parameters:

+ **sort**: _sort the output by metric_ 
+ **limit**: _limit the number of results_ 
+ **desc**: _Pass any value as desc and the output will be reversed (descending)_ 
+ **page**: _When using limit, set the page of results to display_ 

Example request:

```bash
curl -H "Authorization: Bearer <API_KEY>" https://lunarcrush.com/api4/public/stocks/list/v1
```



Example response:

```json
{
  "config": {
    "sort": "market_cap_rank",
    "desc": true,
    "limit": 0,
    "page": 0,
    "total_rows": 2270,
    "generated": 1760647723
  },
  "data": [
    {
      "id": 52199,
      "symbol": "TSM",
      "name": "Taiwan Semiconductor",
      "price": 299.84,
      "volume_24h": 21050629762.120003,
      "percent_change_24h": -1.6277772308096154,
      "market_cap": 1555127087503.36,
      "market_cap_rank": 1,
      "interactions_24h": 6003306,
      "social_volume_24h": 7254,
      "social_dominance": 0.8887364236138763,
      "market_dominance": 1.862154878310016,
      "market_dominance_prev": 1.960328599836193,
      "galaxy_score": 52.3,
      "galaxy_score_previous": 52,
      "alt_rank": 665,
      "alt_rank_previous": 195,
      "sentiment": 81,
      "categories": "technology",
      "last_updated_price": 1760647688,
      "last_updated_price_by": "polygon_market",
      "topic": "tsm taiwan semiconductor",
      "logo": "https://cdn.lunarcrush.com/stocks/tsm.png"
    }
  ]
}
```

Schema:

+ **config**: This includes the inputs for the request processed by the server and may include additional hints about the request and response information.
+ **generated**: A unix timestamp (in seconds) when the data was generated to understand possibly stale data
+ **id**: LunarCrush internal ID for the asset
+ **symbol**: The symbol for the asset
+ **name**: The full name of the asset
+ **price**: Current price in USD
+ **volume_24h**: Volume in USD for 24 hours up to this data point
+ **percent_change_24h**: Percent change in price since 24 hours ago
+ **market_cap**: Total dollar market value of all circulating supply or outstanding shares
+ **market_cap_rank**: The rank of the asset by market cap with additional filtering to remove outliers and bad market data.
+ **interactions_24h**: Number of interactions in the last 24 hours
+ **social_volume_24h**: Total number of posts with interactions on this topic in the last 24 hours
+ **social_dominance**: The percent of the total social volume that this topic represents
+ **market_dominance**: The percent of the total market cap that this asset represents
+ **galaxy_score**: A proprietary score based on technical indicators of price, average social sentiment, relative social activity, and a factor of how closely social indicators correlate with price and volume
+ **galaxy_score_previous**: The galaxy score from the previous 24 hours
+ **alt_rank**: A proprietary score based on how an asset is performing relative to all other assets supported
+ **alt_rank_previous**: The alt rank from the previous 24 hours
+ **sentiment**: % of posts (weighted by interactions) that are positive. 100% means all posts are positive, 50% is half positive and half negative, and 0% is all negative posts.
+ **categories**: an array of categories this topic aggregates into
+ **topic**: LunarCrush social topic. Can only includes letters, numbers, spaces, #, and $
+ **logo**: The URL to the logo for the asset, topic, or category




---

### Stocks

https://lunarcrush.com/api4/public/stocks/:stock/v1

Get market data on a stock. Specify the coin to be queried by providing the numeric ID or the symbol of the coin in the input parameter, which can be found by calling the /coins/list endpoint.

input parameters:

+ **stock**: _provide the numeric id or symbol of the stock._ **required**

Example request:

```bash
curl -H "Authorization: Bearer <API_KEY>" https://lunarcrush.com/api4/public/stocks/7056/v1
```



Example response:

```json
{
  "config": {
    "id": "stocks:7056",
    "name": "NVIDIA Corp.",
    "symbol": "NVDA",
    "topic": "$nvda",
    "generated": 1760647724
  },
  "data": {
    "id": 7056,
    "name": "NVIDIA Corp.",
    "symbol": "NVDA",
    "price": 181.81,
    "market_cap": 4426528070000,
    "percent_change_24h": 0.9620196852582937,
    "volume_24h": 61765001860,
    "close": 181.81,
    "market_cap_rank": 323
  }
}
```

Schema:

+ **config**: This includes the inputs for the request processed by the server and may include additional hints about the request and response information.
+ **id**: LunarCrush internal ID for the asset
+ **name**: The full name of the asset
+ **symbol**: The symbol for the asset
+ **topic**: LunarCrush social topic. Can only includes letters, numbers, spaces, #, and $
+ **generated**: A unix timestamp (in seconds) when the data was generated to understand possibly stale data
+ **price**: Current price in USD
+ **market_cap**: Total dollar market value of all circulating supply or outstanding shares
+ **percent_change_24h**: Percent change in price since 24 hours ago
+ **volume_24h**: Volume in USD for 24 hours up to this data point
+ **close**: Close price for the time period
+ **market_cap_rank**: The rank of the asset by market cap with additional filtering to remove outliers and bad market data.




---

### Stocks Time Series

https://lunarcrush.com/api4/public/stocks/:stock/time-series/v2

Get market time series data on a stock. Specify the stock to be queried by providing the numeric ID or the symbol of the stock in the input parameter, which can be found by calling the /stocks/list endpoint.

input parameters:

+ **stock**: _provide the numeric id or symbol of the stock or token._ **required**
+ **bucket**: _bucket time series data into hours or days. default is hours._ 
+ **interval**: _Use interval to specify the start and end time automatically for convenience. If "start" or "end" parameters are provided this parameter is ignored._ 
+ **start**: _The start time (unix timestamp) to go back to._ 
+ **end**: _The end time (unix timestamp) to stop at._ 

Example request:

```bash
curl -H "Authorization: Bearer <API_KEY>" https://lunarcrush.com/api4/public/stocks/7056/time-series/v2
```



Example response:

```json
{
  "config": {
    "stock": "7056",
    "topic": "$nvda",
    "id": "stocks:7056",
    "name": "NVIDIA Corp.",
    "symbol": "NVDA",
    "interval": "1w",
    "start": 1759968000,
    "end": 1760654924,
    "bucket": "hour",
    "metrics": [],
    "generated": 1760647724
  },
  "data": [
    {
      "time": 1759968000,
      "contributors_active": 5347,
      "contributors_created": 177,
      "interactions": 1472297,
      "posts_active": 8758,
      "posts_created": 230,
      "sentiment": 82,
      "spam": 57,
      "alt_rank": 238,
      "close": 189.11,
      "galaxy_score": 64,
      "high": 189.11,
      "low": 189.11,
      "market_cap": 4607669750000,
      "market_dominance": 5.5528,
      "open": 189.11,
      "social_dominance": 3.4195
    }
  ]
}
```

Schema:

+ **config**: This includes the inputs for the request processed by the server and may include additional hints about the request and response information.
+ **topic**: LunarCrush social topic. Can only includes letters, numbers, spaces, #, and $
+ **id**: LunarCrush internal ID for the asset
+ **name**: The full name of the asset
+ **symbol**: The symbol for the asset
+ **interval**: Typically used for specifying time intervals like 1w = 1 week, 1m = 1 month etc
+ **start**: Start/from unix timestamp (in seconds)
+ **end**: End/to unix timestamp (in seconds)
+ **bucket**: Data is generally bucketed into hours or days
+ **metrics**: Comma separated list of metrics to include or that are included
+ **generated**: A unix timestamp (in seconds) when the data was generated to understand possibly stale data
+ **time**: A unix timestamp (in seconds)
+ **contributors_active**: number of unique social accounts with posts that have interactions
+ **contributors_created**: number of unique social accounts that created new posts
+ **interactions**: number of all publicly measurable interactions on a social post (views, likes, comments, thumbs up, upvote, share etc)
+ **posts_active**: number of unique social posts with interactions
+ **posts_created**: number of unique social posts created
+ **sentiment**: % of posts (weighted by interactions) that are positive. 100% means all posts are positive, 50% is half positive and half negative, and 0% is all negative posts.
+ **spam**: The number of posts created that are considered spam
+ **alt_rank**: A proprietary score based on how an asset is performing relative to all other assets supported
+ **close**: Close price for the time period
+ **galaxy_score**: A proprietary score based on technical indicators of price, average social sentiment, relative social activity, and a factor of how closely social indicators correlate with price and volume
+ **high**: Higest price fo rthe time period
+ **low**: Lowest price for the time period
+ **market_cap**: Total dollar market value of all circulating supply or outstanding shares
+ **market_dominance**: The percent of the total market cap that this asset represents
+ **open**: Open price for the time period
+ **social_dominance**: The percent of the total social volume that this topic represents




---

### Searches Search

https://lunarcrush.com/api4/public/searches/search

Get recently popular social posts matching a single search term or phrase. Optionally configure and test a custom search configuration.

input parameters:

+ **term**: _Test a single search term or phrase_ 
+ **search_json**: _A JSON object (stringified) that defines the search criteria for the custom search aggregation. Posts that match any of the search term will be included. For each search term there are optional inclusion and exclusion terms to help fine tune the results._ 

Example request:

```bash
curl -H "Authorization: Bearer <API_KEY>" https://lunarcrush.com/api4/public/searches/search
```



Example response:

```json
{
  "error": "Error: search_json object is not formatted correctly"
}
```

Schema:





---

### Searches List

https://lunarcrush.com/api4/public/searches/list

List all custom search aggregations.

Example request:

```bash
curl -H "Authorization: Bearer <API_KEY>" https://lunarcrush.com/api4/public/searches/list
```



Example response:

```json
{
  "data": [
    {
      "id": "lc1s5M27Jq",
      "name": "Pump.fun Leaderboard",
      "search_json": {
        "terms": [],
        "rollups": [
          "5emfxsydsscpnu63wtpprjbbr5ybjmsenzgrvtuppump"
        ]
      },
      "priority": true,
      "created": 1749064987
    }
  ]
}
```

Schema:

+ **id**: LunarCrush internal ID for the asset
+ **name**: The full name of the asset




---

### Searches Create

https://lunarcrush.com/api4/public/searches/create

Create a custom search aggregation of topics and search terms. Fine tune the posts that get included or excluded. Search terms and configuration cannot be changed once created. If successful returns the new id/slug and the processed search config. Note that search terms will be adjusted and simplified for optimized search and matching.

input parameters:

+ **name**: _The name of the custom search aggregation._ **required**
+ **search_json**: _A JSON object (stringified) that defines the search criteria for the custom search aggregation. Search terms and configuration cannot be changed once created. Posts that match any of the search term will be included. For each search term there are optional inclusion and exclusion terms to help fine tune the results._ **required**
+ **priority**: _Flag as a high priority search aggregation. Pro accounts get up to 10 high priority search aggregations at a time._ 

Example request:

```bash
curl -H "Authorization: Bearer <API_KEY>" https://lunarcrush.com/api4/public/searches/create
```



Example response:

```json
{
  "error": "Error: name is required"
}
```

Schema:





---

### Searches Update

https://lunarcrush.com/api4/public/searches/:slug/update

Update a custom search aggregation name or priority. Search terms and configuration cannot be changed once created.

input parameters:

+ **slug**: _The ID of the custom search aggregation to update._ **required**
+ **name**: _The name of the custom search aggregation._ 
+ **search_json**: _A JSON object (stringified) that defines the search criteria for the custom search aggregation. Search terms and configuration cannot be changed once created. Posts that match any of the search term will be included. For each search term there are optional inclusion and exclusion terms to help fine tune the results._ **required**
+ **priority**: _Define if this is a high priority search aggregation. Pro accounts get up to 10 high priority search aggregations at a time._ 

Example request:

```bash
curl -H "Authorization: Bearer <API_KEY>" https://lunarcrush.com/api4/public/searches/:slug/update
```



Example response:

```json
{
  "error": "Error: search_json is required"
}
```

Schema:





---

### Searches Delete

https://lunarcrush.com/api4/public/searches/:slug/delete

Delete a custom search aggregation.

input parameters:

+ **slug**: _The ID of the custom search aggregation to delete._ **required**

Example request:

```bash
curl -H "Authorization: Bearer <API_KEY>" https://lunarcrush.com/api4/public/searches/:slug/delete
```



Example response:

```json
{
  "error": "Error: That item does not exist"
}
```

Schema:





---

### Searches

https://lunarcrush.com/api4/public/searches/:slug

See the summary output of a custom search aggregation.

input parameters:

+ **slug**: _The ID of the custom search aggregation to view._ **required**

Example request:

```bash
curl -H "Authorization: Bearer <API_KEY>" https://lunarcrush.com/api4/public/searches/:slug
```



Example response:

```json
{
  "error": "Use the topics endpoints to get the latest data like /public/topic/:slug/v1"
}
```

Schema:





---

### System Changes

https://lunarcrush.com/api4/public/system/changes

Updates to potential changes to historical time series data. Search term changes only impact the most recent 72 hours (hourly) or 3 days (daily) data. "full historical" is a change that may impact the full history of data. Each change provides a description of what is impacted and why.

Example request:

```bash
curl -H "Authorization: Bearer <API_KEY>" https://lunarcrush.com/api4/public/system/changes
```



Example response:

```json
{
  "data": [
    {
      "asset_type": "coins",
      "asset_id": 161780,
      "asset_name": "MeowChi (MEOWCHI)",
      "change": "search terms established",
      "description": "search criteria initially set for this asset for the purposes of tracking changes over time",
      "time": 1760646657
    }
  ]
}
```

Schema:

+ **asset_type**: One of coins, nfts, stocks, topic or category
+ **asset_id**: The id of the asset (coin, nft, stock, topic, or category)
+ **asset_name**: The descriptive name of the asset to help identify it
+ **change**: The type of change that occurred
+ **description**: Explanation of the change and the potential impact
+ **time**: A unix timestamp (in seconds)
