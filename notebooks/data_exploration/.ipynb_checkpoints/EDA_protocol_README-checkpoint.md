# Exploratory Data Analysis protocol
A standardized protocol for exploring data, and selecting/engineering features.

## Inspect data

<hr style="border: 4px dotted #aaaaaa; border-style: none none dotted; color: #fff; background-color: #fff;"/>

### Zeroth-Order inspection: data properties

From the raw data itself, look for: 
* **structure**/**format**: tabular or non-relational (ie how are features and values stored?)
* **feature count**
    * too many features $\to$ need to likely reduce
* **feature types**: quantitative and qualitative (ie how are features represented?)
    * multiple variable types - continuous, dicrete, and categorical
    * multiple data types - int, string, float, datetime
    * consider mapping categorical features to values
* **fill rate**: NaNs/missing vals (empty or '-1'-type?)
    * check for frequency of NaNs
        * consider dropping feature if too many missings w.r.t threshold
            * if so, how important is the missing data?
    * consider if missing data is missing for a reason or just randomly dropped
        * if a reason or pattern, then consider if it is sensible that it is missing
    * (**advanced**) for important categories, it may be useful to fill in the missing data
        * dummy values (0 or "None")
        * most frequent value if makes sense
        * interpolations: compute distribution, sample from it $\to$ _dubious!!!_
* Useful commands
    * for tabular data, `pandas.DataFrame.info()` 
        * tells how many non-null rows for each column (_ie_ feature)
        * tells the data type for each column

<hr style="border: 4px dotted #aaaaaa; border-style: none none dotted; color: #fff; background-color: #fff;"/>

## First-order inspection: feature properties

For all quantitative (numerical) features, look at
* statistical measures (**stats**)
    * mean, std, median, quantiles, mins/maxs
    * Useful commands
        * for tabular data, `pandas.DataFrame.describe()` 
* **distributions**
    * when possible, characterize distributions (type of distn)

        * <img src="house-prices-2/notebooks/distplot_of_target.png" alt="drawing" width="500"/>

        * <img src="boston-reloaded/notebooks/distributions_and_boxplot.png" alt="drawing" width="500"/>

    * consider whether discrete or continuous
    * consider whether any seems to match the target feature distribution
    * `df.hist()` will do this with any number of columns
    
    * <img src="boston-reloaded/notebooks/multiple_distplots.png" alt="drawing" width="500"/>

* useful commands
    * for tabular data, `pandas.DataFrame.describe()` 
        * works _only_ for numerical data
        * tells statistical measures for each column (_ie_ feature) of numerical data

**note** it is possible to also include categorical data here
    
<hr style="border: 4px dotted #aaaaaa; border-style: none none dotted; color: #fff; background-color: #fff;"/>

## Second-order inspection: relationships between features

Quantify relationships between features, as part of the _feature **selection**_ as well as _feature **engineering**_ processes

* Identify **target feature(s)**
* check **target correlations** between features and target feature(s)
    * test for and remove outliers when necessary
    * quick inspections
        * barcharts (quick visual)
        * <img src="boston-reloaded/notebooks/correlation_with_target_barchart.png" alt="drawing" width="400"/>
    * pairwise scatterplots are good to check the nature of the correlation
        * `sns.pairplot(df)`
        * <img src="house-prices-2/notebooks/pairplots_with_target.png" alt="drawing" width="500"/>
 
* check **pair correlations** between all feature pairs (without target)
    * test for and remove outliers when necessary
    * test for correlated features in order to reduce the number of features
    * pair-correlation matrix for quick inspection
        * `sns.heatmap(df.drop('target_feature', axis=1).corr())`
        * <img src="wine-quality/notebooks/correlation_matrix_with_target.png" alt="drawing" width="400"/>

        `![](wine-quality/notebooks/correlation_matrix_with_target.png  =250x)`

        * can also limit the columns to those of the largest values for a smaller matrix
    * look for features which are correlated with the target, but also together
        * this allows to remove redundant information and simplify the data
        
        * <img src="wine-quality/notebooks/pairplots_with_hued_kde.png" alt="drawing" width="400"/>
        
        * `![](wine-quality/notebooks/pairplots_with_hued_kde.png  =250x)`
    
    * pairwise scatterplots are good to check the nature of the correlation
        * `sns.pairplot(df)`
    * for categorical features, 
        * compute a histogram per category
            * `df.groupby('test_feature')['target_feature'].count().plot(type='bar')`
        * also useful, is to plot the distibution of each category
            * `sns.boxplot(x="test_feature", y="target_feature", data=df)`
            * alternatively, use `sns.violinplot(x="test_feature", y="target_feature", data=df)`
                * this uses KDE to plot the density distribution
            * alternatively, use `sns.swarmplot(x="test_feature", y="target_feature", data=df)`
                * gives an idead of the distribution of values, 
                * does not scale well to large counts $\to$ collisions on limits
        * <img src="boston-reloaded/notebooks/categorical_distributions.png" alt="drawing" width="500"/>


