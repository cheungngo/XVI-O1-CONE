# CHECKPOINT v12 (started 2026-10-19 04:38 UTC)
## Step 0: v11 chmod 444; frozen hashes logs/frozen_v12_before.sha (unchanged vs v11: ec965c15/0df9a0d1/57187bc6); v9-v11 hashes logs/v11_hashes_before_v12.sha.
## Step 1: skeleton v12src + code/build_v12.py; skeleton compiles.
## Step 2 (item 6) DONE: registry 04:40 UTC same length as new_oct18g, 16 differing chars (SSR timestamp), 258 ids identical -> no new_oct19b. logs/v12/registry_oct19b.sha
## Step 3 (item 4) running: code/v12/wall_certificate.py (v8 cert, output path only changed), setsid walls_driver.sh, 6 runs (1/3,1/2,2/3 x CR,F) -> logs/v12/walls/
## Step 4 (item 1) KEY FIND: code/v12/phi_asym_fit.py (odd powers absent), structure_test.py (R_d(h)/(d^2(d^2-4)) d-independent, 20 digits),
 PSLQ -> CLOSED FORM (identified): F(mu,nu) = h^3/3 + (d^2/6-1/3)h + d^2(d^2-4)[P(h) - h^2(h^2-1)psi1(h)/48], P = h^3/48+h^2/96-5h/288-1/96.
 code/v12/F_closed.py: agrees with all 414 cached quadrature values, max rel 4.8e-28 (logs/v12/F_closed.json). d=2 -> polynomial.
 Pole: a4(d) = d^2(d^2-4)/240 -> P0 (d=1) pole 2*alpha*a4 = -alpha/40 (exact given closed form).
## Step 5 (item 1): code/v12/m10_exact.py -> logs/v12/m10_exact_dps40.json: M10 to 40 digits (K300/J36 vs K600/J48 agree 1e-34..1e-41)
 for P0 (Rh,Rk,Rmu,Rnu) and P1 (Rh,Rk) at 3/10, 7071/10000, 1/2, 1. Agrees with v11 within v11 errors. P0 Rh: 3/10 0.11574388259581850963848639109243,
 7071/1e4 -0.04322206410166229544037429665527. code/v12/counterterm.py: FP_Rk - FP_Rw = c4 log s + sum_{m=1..4} (-1)^{m+1} t^m/m c_{4-m}, verified 1e-39;
 R_h - R_mu = alpha/32. code/v12/m10_pslq.py: alpha=1 Rh: M=(1-40log2-20gamma)/800; Rk: -(6+10log2+5gamma)/200; alpha=1/2 Rh: (1-40log2-20gamma)/1600,
 Rk: -(6+15log2+5gamma)/400; no credible relation at 3/10, 7071/1e4. XVI-P prescription = DRED+MSbar+N4 (local ambiguity fixed by normalization): no cone mode regulator induced.
## Step 6: sec_v12.tex written (closed form, pairing, counterterm, M10 table, walls placeholders, open, changes); compiles.
## Step 7 (item 4) DONE: walls (exact Q(i), DM=6): 1/3 CR,F: N=35 rank 27 dimZ 8; 1/2 CR=F: N=42 rank 33 dimZ 9; 2/3 CR: N=35 rank 27 dimZ 8;
 2/3 F: N=39 rank 30 dimZ 9. B subset Z, B in span everywhere. code/artifacts_v12.py written (earlier-version comparison fixed; 16 files unchanged).
## Step 8: abstract, release items, scope, opentable, walls_text finalised. Items 2,3,5 recorded OPEN with obstructions.
## Step 9: final append before hashing: make_tables, artifacts_v12, build_v12, pdflatex until stable, SHA256SUMS_v12. No append after this line.
