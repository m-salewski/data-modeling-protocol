# Data exploration protocol
A standardized protocol for exploring data, and selecting/engineering features.

## Inspect data

### Zeroth-Order inspection: data properties

From the raw data itself, look for: 
* what is structure/format: tabular or non-relational (ie how are features and values stored?)
* data types: quantitative and qualitative (ie how are features represented?)
    * consider mapping categorical features to values
* Count the number of features
    * too many features $\to$ need to likely reduce
* NaNs/missing vals (empty or '-1'-type?)
    * check for frequency of NaNs
        * consider dropping feature if too many missings w.r.t threshold
            * if so, how important is the missing data?
    * consider if missing data is missing for a reason or just randomly dropped
        * if a reason or pattern, then consider if it is sensible that it is missing
    * (**advanced**) for important categories, it may be useful to fill in the missing data
        * dummy values
        * interpolations
            
## First-order inspection: feature properties

For all quantitative (numerical) features, look at
* Identify target features
* statistical measures
    * mean, std, median, quantiles, mins/maxs
* distributions
    * when possible, characterize distributions (type of distn)
    * consider whether discrete or continuous
    * consider whether any seems to match the target feature distribution

**note** it is possible to also include categorical data here
    
## Second-order inspection: relationships between features

Quantify relationships between features

* part of the _feature selection_ as well as _feature engineering_ processes
* check correlations between features and target feature(s)
    * test for and remove outliers when necessary
    * confusion matrix for quick inspection
        * `sns.heatmap(df.corr())`   
    * pairwise scatterplots are good to check the nature of the correlation
        * `sns.pairplot(df)`
* check correlatiosn between all feature pairs (without target)
    * test for and remove outliers when necessary
    * confusion matrix for quick inspection
        * `sns.heatmap(df.drop('target_feature', axis=1).corr())`
        * can also limit the columns to those of the largest values for a smaller confusion matrix
    * look for features which are correlated with the target, but also together
        * this allows to remove redundant information and simplify the data
    * pairwise scatterplots are good to check the nature of the correlation
        * `sns.pairplot(df)`
   


