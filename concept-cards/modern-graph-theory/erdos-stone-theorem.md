---
concept: "Erdős-Stone Theorem"
slug: erdos-stone-theorem
category: extremal-graph-theory
subcategory: fundamental-theorems
tier: advanced
source: "Modern Graph Theory"
source_slug: modern-graph-theory
authors: "Béla Bollobás"
chapter: "Extremal Problems"
chapter_number: 4
pdf_page: 110
section: "IV.4 The Structure of Graphs"
extraction_confidence: high
aliases:
  - "Theorem 22"
  - "Bollobás-Erdős theorem"
  - "fundamental theorem of extremal graph theory"
prerequisites:
  - turans-theorem
  - extremal-function
extends:
  - turans-theorem
related:
  - szemeredis-regularity-lemma
contrasts_with: []
answers_questions:
  - "What is the Erdős-Stone theorem?"
---

# Quick Definition
If $e(G) \ge (1 - 1/r + \varepsilon)\binom{n}{2}$, then $G$ contains $K_{r+1}(t)$ for $t \ge c \log n$, where $K_{r+1}(t)$ is a complete $(r+1)$-partite graph with $t$ vertices per class.

# Core Definition
**Theorem 22** (Bollobás-Erdős, 1973; strengthening Erdős-Stone, 1946): Let $r \ge 1$ and $\varepsilon > 0$. If $|G| = n$ is large enough and $e(G) \ge (1-1/r+\varepsilon)\binom{n}{2}$, then $G \supset K_{r+1}(t)$ for some $t \ge \varepsilon \log n / (2^{r+1}(r-1)!)$ (Bollobás, p. 136).

# Prerequisites
- **Turán's theorem** — The base case; Erdős-Stone extends it
- **Extremal function** — Determines $ex(n;F)$ asymptotically

# Key Properties
1. Called "the fundamental theorem of extremal graph theory" (p. 133)
2. Determines $ex(n;F)$ asymptotically for any non-bipartite $F$
3. $ex(n;F) = (1-1/r)\binom{n}{2} + o(n^2)$ where $r+1 = \chi(F)$ (Corollary 23)
4. The logarithmic growth of $t$ is optimal (shown in Chapter VII)
5. Proof uses induction on $r$ and double counting

# Construction / Recognition
1. Check $e(G) \ge (1-1/r+\varepsilon)\binom{n}{2}$
2. Find subgraph $H$ with $\delta(H) \ge (1-1/r+\varepsilon/2)|H|$ (Lemma 21)
3. Use induction to find $K_{r+1}(t)$

# Context & Application
"The Erdős-Stone theorem is rightly called the fundamental theorem of extremal graph theory" (p. 133). It asymptotically solves the forbidden subgraph problem for all non-bipartite graphs.

# Examples
**Example** (pp. 134-135): For $r = 1$: if $\delta(G) \ge \varepsilon n$ and $G$ has no $K_2(t)$, double counting gives $n\binom{\varepsilon n}{t} < t\binom{n}{t}$, which fails for $t = \lceil\varepsilon \log n\rceil$.

# Relationships
## Builds Upon
- **turans-theorem** — Extended

## Enables
- **asymptotic-extremal-function** — Corollary 24
- **upper-density-theorem** — Corollary 25

## Related
- **szemeredis-regularity-lemma** — Alternative proof approach

# Common Errors
- **Error**: Applying the theorem to bipartite forbidden graphs
  **Correction**: For bipartite $F$, $\chi(F) = 2$, so $r = 1$ and the theorem gives $ex(n;F) = o(n^2)$, which is weak

# Common Confusions
- **Confusion**: Thinking the theorem gives exact values of $ex(n;F)$
  **Clarification**: It gives asymptotic values; the error term is $o(n^2)$

# Source Reference
Chapter IV, Section IV.4, pages 133-138. Theorem 22.

# Verification Notes
- Definition source: Direct theorem statement from p. 136
- Confidence rationale: Major theorem with complete proof
- Uncertainties: None
- Cross-reference status: Verified
