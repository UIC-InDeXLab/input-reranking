This project contains differnet subdirectories:

- './figures': contains the plots and reports generated for the paper.
- './data': contains the csv files which are the results of experiment runs.
- './tasks': contains specific code for each Task, like Graph Degree Task and Query Database Task.
    - './tasks/db': contains two notebooks, 
        - 'db_queries:1.ipynb' runs the first part of algorithms, where the relevance estimations are observed from different helper models then the inputs are ranked based on those.
        - 'db_queries:2.ipynb' runs the second part which is asking the reranked elements from the LLM.
    - './tasks/graph': contains two notebooks like './tasks/db'.
- 'utils': contains the speicfic implementations of Bipartite algorithm and also some utility functions for API calls to LLMs.
- 'initial_obsevation.ipynb': This notebooks gets the output error of the LLM given different graph sizes for the Graph Degree Task.