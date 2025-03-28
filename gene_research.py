from gprofiler import GProfiler


def research(genes_list: list):
    
    gp: GProfiler = GProfiler(return_dataframe=True)

    results = gp.profile(organism="hsapiens", query=genes_list)

    return results