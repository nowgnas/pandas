from importFile import *

titanic = sns.load_dataset("titanic")


# print(titanic.info())
def count_missing(vec):
    null_vec = pd.isnull(vec)
    null_count = np.sum(null_vec)
    return null_count


def prop_missing(vec):
    num = count_missing(vec)
    dem = vec.size
    return num / dem


cmis_col = titanic.apply(count_missing)
# print(cmis_col)
pmis_col = titanic.apply(prop_missing)


# print(pmis_col)
def prop_complete(vec):
    return 1 - prop_missing(vec)


