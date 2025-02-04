# Exploratory Data Analysis protocol
A standardized protocol for exploring data, and selecting/engineering features.

> **Because EDA is Tedious and Takes Forever**

> We’re all guilty of performing a cursory EDA, if any at all (“let’s just get to the model training!”). [...] EDA can take a considerable amount of setup. Coding those same, slightly modified functions for the hundredth time is something we all do. And remembering which visualization types work best for which feature types and feature/target-type combination is not easy.

## Inspect data

<hr style="border: 4px dotted #aaaaaa; border-style: none none dotted; color: #fff; background-color: #fff;"/>

### Zeroth-Order inspection: data properties

From the raw data itself, look for: 
* **structure**/**format**: tabular or non-relational (ie how are features and values stored?)
* **feature count**
    * too many features $\to$ need to likely reduce
        * having more features increases the likelihood of overfitting
* **feature types**: quantitative and qualitative (ie how are features represented?)
    * multiple variable types - continuous, dicrete, and categorical
    * multiple (raw) data types - int, string, float, datetime
    * consider mapping categorical features to values - _tranforms_
    * further breakdown of types (from `mlmachine`):
        * `'boolean'`
        * `'nominal'`: an integer classification
        * `'ordinal'`: an ordered integer classification
        * `'continuous'`: float
        * `'count'`: continuous integer
        * `'string'`: (classifier, likely to be encoded)
        * `'date'`
        * `'category'`: a string classification
        * `'number'`: also an int classification
        * **Note** some variables can be more than one of these types, _e.g._ a coded cataegory as nominal.
    * **Note** when dealing with different feature types, they will need to be pre-processed before they are re-combined ino the model 
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
        * see [Imputing](https://scikit-learn.org/stable/modules/impute.html#impute)
* Useful commands
    * for tabular data, `pandas.DataFrame.info()` 
        * tells how many non-null rows for each column (_ie_ feature)
        * tells the data type for each column

<hr style="border: 4px dotted #aaaaaa; border-style: none none dotted; color: #fff; background-color: #fff;"/>

**Note** some packages classify these types and do the fill-analysis already.
    * `pandas-profiling`: see [pandas-profiling-feature-pravin-borate](https://www.linkedin.com/pulse/pandas-profiling-feature-pravin-borate/)

## First-order inspection: feature properties

For all quantitative (numerical) features, look at
* statistical measures (**stats**)
    * mean, std, median, quantiles, mins/maxs
    * Useful commands
        * for tabular data, `pandas.DataFrame.describe()` 
        
* **distributions**
    * when possible, characterize distributions (type of distn)

        * <img src="figures/distplot_of_target.png" alt="drawing" width="500"/>

        * <img src="figures/distributions_and_boxplot.png" alt="drawing" width="500"/>

    * consider whether discrete or continuous
    * consider whether any seems to match the target feature distribution
    * `df.hist()` will do this with any number of columns
    
    * <img src="figures/multiple_distplots.png" alt="drawing" width="500"/>

* **variance** 
    * 

* useful commands
    * for tabular data, `pandas.DataFrame.describe()` 
        * works _only_ for numerical data
        * tells statistical measures for each column (_ie_ feature) of numerical data

**note** it is possible to also include categorical data here
    
<hr style="border: 4px dotted #aaaaaa; border-style: none none dotted; color: #fff; background-color: #fff;"/>

## Second-order inspection: relationships between features

### Quantitative relationships

Quantify relationships between features, as part of the _feature **selection**_ as well as _feature **engineering**_ processes

* Identify **target feature(s)**
* check **target correlations** between features and target feature(s)
    * test for and remove outliers when necessary
    * quick inspections
        * barcharts (quick visual)
        * <img src="figures/correlation_with_target_barchart.png" alt="drawing" width="400"/>
    * pairwise scatterplots are good to check the nature of the correlation
        * `sns.pairplot(df)`
        * <img src="figures/pairplots_with_target.png" alt="drawing" width="500"/>
 
* check **pair correlations** between all feature pairs (without target)
    * test for and remove outliers when necessary
    * test for correlated features in order to reduce the number of features
        * _ie_ **multicollinearity** :
            * a characteristic of the data matrix $X$ where a predictive feature can be linearly estimated from others
            * $X$ has less than full rank
                * $X$ is _ill-conditioned_, the coefficient estimates of the multiple regression may change erratically in response to small changes in the model or the data
                * the moment matrix $X^{\mathsf {T}}X$ cannot be inverted. 
                * _e.g._ for a general linear model $y=X\beta +\epsilon$, the ordinary least squares estimator $\hat {\beta }_{OLS}=(X^{\mathsf {T}}X)^{-1}X^{\mathsf {T}}y$ does not exist.            
            * only affects calculations of individual predictors: a multivariate regression model with collinear predictors can indicate how well the entire bundle of predictors predicts the outcome variable, but it may not give valid results about any individual predictor, or about which predictors are redundant with respect to others.   
        * can remedy (or try) with _PCA_, which aggregates features in statistically meaningful ways into linearly independent features; the problem is that it can obscure interpretability
    * pair-correlation matrix for quick inspection
        * `sns.heatmap(df.drop('target_feature', axis=1).corr())`
        * <img src="figures/correlation_matrix_with_target.png" alt="drawing" width="400"/>

        `![](figures/correlation_matrix_with_target.png  =250x)`

        * can also limit the columns to those of the largest values for a smaller matrix
    * look for features which are correlated with the target, but also together
        * this allows to remove redundant information and simplify the data
        
        * <img src="figures/pairplots_with_hued_kde.png" alt="drawing" width="400"/>
        
        * `![](figures/pairplots_with_hued_kde.png  =250x)`
    
    * pairwise scatterplots are good to check the nature of the correlation
        * `sns.pairplot(df)`
        
        * <img src="../extras/figures/pairplots_with_bars_contours_and_scatters.png" alt="drawing" width="500"/>

        `![](figures/correlation_matrix_with_target.png  =250x)`        
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
        * <img src="figures/categorical_distributions.png" alt="drawing" width="500"/>

## Third-order inspection: 

### Qualitative relationships
 
Some features may be present in the data which have absolutely little or no value.
