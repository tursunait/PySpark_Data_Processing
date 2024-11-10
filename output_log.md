## Operation: Read CSV

**Output:**
Loaded data from /Users/tusunaiturumbekova/PySpark_Data_Processing/data/customer_feedback_satisfaction.csv. Showing first few rows:

## Operation: Show Data

**Output:**
None

## Operation: Summary Statistics

**Output:**
|    | summary   |        Age |   Income |   PurchaseFrequency |   SatisfactionScore |
|---:|:----------|-----------:|---------:|--------------------:|--------------------:|
|  0 | count     | 38444      |  38444   |         38444       |          38444      |
|  1 | mean      |    43.4969 |  75076.6 |            10.4539  |             85.2764 |
|  2 | stddev    |    14.9727 |  25975.8 |             5.76562 |             16.8986 |
|  3 | min       |    18      |  30001   |             1       |              4.28   |
|  4 | max       |    69      | 119999   |            20       |            100      |

## Operation: Average Satisfaction by Country

**Query:**
```

        SELECT Country, AVG(SatisfactionScore) AS Avg_Satisfaction
        FROM customer_feedback
        GROUP BY Country
        ORDER BY Avg_Satisfaction DESC
    
```

**Output:**
|    | Country   |   Avg_Satisfaction |
|---:|:----------|-------------------:|
|  0 | Canada    |            85.4131 |
|  1 | USA       |            85.3798 |
|  2 | France    |            85.2631 |
|  3 | Germany   |            85.2617 |
|  4 | UK        |            85.0616 |

## Operation: Read CSV

**Output:**
Loaded data from /Users/tusunaiturumbekova/PySpark_Data_Processing/data/customer_feedback_satisfaction.csv. Showing first few rows:

## Operation: Show Data

**Output:**
None

## Operation: Summary Statistics

**Output:**
|    | summary   |        Age |   Income |   PurchaseFrequency |   SatisfactionScore |
|---:|:----------|-----------:|---------:|--------------------:|--------------------:|
|  0 | count     | 38444      |  38444   |         38444       |          38444      |
|  1 | mean      |    43.4969 |  75076.6 |            10.4539  |             85.2764 |
|  2 | stddev    |    14.9727 |  25975.8 |             5.76562 |             16.8986 |
|  3 | min       |    18      |  30001   |             1       |              4.28   |
|  4 | max       |    69      | 119999   |            20       |            100      |

## Operation: Average Satisfaction by Country

**Output:**
|    | Country   |   Avg_Satisfaction |
|---:|:----------|-------------------:|
|  0 | Canada    |            85.4131 |
|  1 | USA       |            85.3798 |
|  2 | France    |            85.2631 |
|  3 | Germany   |            85.2617 |
|  4 | UK        |            85.0616 |

![Average Satisfaction by Country](
        SELECT Country, AVG(SatisfactionScore) AS Avg_Satisfaction
        FROM customer_feedback
        GROUP BY Country
        ORDER BY Avg_Satisfaction DESC
    )

## Operation: Plot Correlation Matrix

**Output:**
Correlation matrix plot displayed.

## Operation: Plot Satisfaction Distribution

**Output:**
Distribution plot displayed for Satisfaction Scores.

## Operation: End Spark Session

**Output:**
Spark session stopped.

## Operation: Average Satisfaction by Country

**Output:**
<MagicMock name='mock.sql().toPandas().to_markdown()' id='5358246592'>

![Average Satisfaction by Country](
        SELECT Country, AVG(SatisfactionScore) AS Avg_Satisfaction
        FROM customer_feedback
        GROUP BY Country
        ORDER BY Avg_Satisfaction DESC
    )

## Operation: End Spark Session

**Output:**
Spark session stopped.

## Operation: Plot Satisfaction Distribution

**Output:**
Distribution plot displayed for Satisfaction Scores.

## Operation: Show Data

**Output:**
<MagicMock name='mock.show()' id='6020138432'>

## Operation: Summary Statistics

**Output:**
<MagicMock name='mock.describe().toPandas().to_markdown()' id='6021562288'>

## Operation: Average Satisfaction by Country

**Output:**
<MagicMock name='mock.sql().toPandas().to_markdown()' id='5758902128'>

![Average Satisfaction by Country](
        SELECT Country, AVG(SatisfactionScore) AS Avg_Satisfaction
        FROM customer_feedback
        GROUP BY Country
        ORDER BY Avg_Satisfaction DESC
    )

## Operation: End Spark Session

**Output:**
Spark session stopped.

## Operation: Plot Satisfaction Distribution

**Output:**
Distribution plot displayed for Satisfaction Scores.

## Operation: Show Data

**Output:**
<MagicMock name='mock.show()' id='6078552240'>

## Operation: Summary Statistics

**Output:**
<MagicMock name='mock.describe().toPandas().to_markdown()' id='5516433248'>

