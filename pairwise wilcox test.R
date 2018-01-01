
pairwise_wilcox_test <- function(df, attribute,grouping_name){

  df <- as.data.frame(df)
  df$group <- df[, grouping_name]
  
  print(pairwise.wilcox.test(df$attribute, df$group))
}