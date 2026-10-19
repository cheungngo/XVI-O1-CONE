import os,hashlib
C='/workspace/XVI-O1-CONE/code'
groups=[
("Apex BRST jets and cohomology (v1--v3)",["apex_jets.py","apex_jets_v1_frozen.py","apex_run.py","tri_count.py","tri_count_all.py","tri_run.py","tri_run_all.py","resonances.py","inner_degrees.py","inner_degrees_q24.py","locality.py"]),
("Flat-space controls",["flat_count.py","flat_pole.py","flat_vs_p18.py"]),
("Kernels, coincidence limits and heat coefficients",["kernel.py","tensor.py","coinc.py","xcheck_coinc.py","heatcoef.py","weighted_apex.py","weighted_checks.py"]),
("Tadpoles D02, D12, D05a and the hh structures",["cone_tadpole.py","tadpole2.py","tadpole2_fast.py","hh_structures.py"]),
("Spectral apex reduction of the bubbles (v4)",["spectral_apex.py","spec_compare.py","catalogue_check.py"]),
("Slavnov--Taylor and Ward diagnostics",["st_test_const.py","st_scan.py","st_norm.py","st_v6.py","st_v6_stats.py","ward_scan.py","ward_xcheck.py"]),
("H_I obstruction for D01 (v6)",["hi_d01.py","hi_d01_exact.py"]),
("Build and artifact scripts for v6",["build_v6.py","artifacts_v6.py"]),
("Debug scratch",["dbg.py","dbg2.py"]),
]
allf=set(f for f in os.listdir(C) if f.endswith('.py')); used=set(f for g in groups for f in g[1]); assert allf==used,(allf-used,used-allf)
o=[r"""\documentclass[10pt]{article}
\usepackage[margin=2cm]{geometry}\usepackage[T1]{fontenc}\usepackage{lmodern}\usepackage{xcolor}\usepackage{listings}\usepackage{hyperref}
\lstset{language=Python,basicstyle=\ttfamily\scriptsize,breaklines=true,columns=fullflexible,keepspaces=true,showstringspaces=false,numbers=left,numberstyle=\tiny\color{gray},keywordstyle=\color{blue!60!black},commentstyle=\color{green!40!black},stringstyle=\color{red!50!black},frame=single,upquote=true}
\title{XVI-O1-CONE: Python scripts (v1--v6)}\author{Ngo Cheung}\date{18 October 2026}
\begin{document}\maketitle
\noindent All Python scripts in \texttt{/workspace/XVI-O1-CONE/code/} used for XVI-O1-CONE v1--v6, grouped by purpose and reproduced verbatim. Each listing carries its SHA-256. The scripts import from one another and read frozen XVI-P/XVI-Q engine files and run logs that are not included here.
\tableofcontents
"""]
for t,fs in groups:
  o.append("\\section{%s}\n"%t)
  for f in fs:
    s=open(os.path.join(C,f)).read(); h=hashlib.sha256(s.encode()).hexdigest()
    assert '\\end{lstlisting}' not in s
    o.append("\\subsection{\\texttt{%s}}\n\\noindent{\\scriptsize SHA-256: \\texttt{%s}}\n\\begin{lstlisting}\n%s\n\\end{lstlisting}\n"%(f.replace('_','\\_'),h,s.rstrip()))
o.append("\\end{document}\n")
open('XVI-O1-CONE-scripts.tex','w').write(''.join(o))
