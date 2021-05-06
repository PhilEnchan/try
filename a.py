import dot2tex
testgraph = """
digraph G {
    graph [mindist=0.5];
    node [fixedsize=true, shape=circle, width=0.4, style="fill=green!20"];
    c -> n_1 [style="-stealth"];
    c -> n_2 [style="-to"];
    c -> n_3 [style="-latex"];
    c -> n_4 [style="-diamond"];
    c -> n_5 [style="-o"];
    c -> n_6 [style="{-]}"];
    c -> n_7 [style="-triangle 90"];
    c -> n_8 [style="-hooks"];
    c -> n_9 [style="->>"];
    c [style="fill=red!80"];
}
"""
texcode = dot2tex.dot2tex(testgraph, format='tikz', crop=True)