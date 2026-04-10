---
concept: Deletion-Contraction
slug: deletion-contraction
category: tutte-polynomial
subcategory: null
tier: foundational
source: "Modern Graph Theory"
source_slug: modern-graph-theory
authors: "Béla Bollobás"
chapter: "The Tutte Polynomial"
chapter_number: 10
pdf_page: 341
section: "X.1 Basic Properties of the Tutte Polynomial"
extraction_confidence: high
aliases:
  - "cut and fuse"
  - "edge deletion and contraction"
prerequisites: []
extends: []
related:
  - tutte-polynomial
  - rank-generating-polynomial
  - chromatic-polynomial
contrasts_with: []
answers_questions:
  - "How do I compute the Tutte polynomial using deletion-contraction?"
  - "How do I compute the chromatic polynomial of a graph?"
---

# Quick Definition
Deletion ($G - e$) removes an edge $e$ from $G$; contraction ($G/e$) shrinks $e$ to identify its endpoints. The Tutte polynomial satisfies $T_G = T_{G-e} + T_{G/e}$ when $e$ is neither a bridge nor a loop.

# Core Definition
Given $G = (V, E)$ and $e \in E$: "let $G - e = (V, E - \{e\})$" (deletion) and "let $G/e$ be the multigraph obtained from $G$ by fusing (contracting) the edge $e$" so that its endpoints $u, v$ are replaced by a single vertex $w = (uv)$, with all other edges redirected accordingly (Bollobás, p. 341). The Tutte polynomial satisfies: $T_G = x T_{G-e}$ (bridge), $T_G = y T_{G-e}$ (loop), $T_G = T_{G-e} + T_{G/e}$ (otherwise). The chromatic polynomial satisfies the related formula $p_G(x) = p_{G-e}(x) - p_{G/e}(x)$ (cf. Ch V, p. 156).

# Prerequisites
This is a foundational concept -- no prerequisites beyond basic multigraph definitions.

# Key Properties
1. Deletion: $G - e$ has the same vertices, one fewer edge
2. Contraction: $G/e$ identifies the endpoints of $e$, has one fewer vertex and one fewer edge
3. If $e$ is a loop: $G/e = G - e$
4. If $e$ is a bridge: $T_{G-e} = T_{G/e}$
5. Both $G - e$ and $G/e$ have exactly one fewer edge than $G$
6. Every element of $E - \{e\}$ corresponds to a unique element of $E(G/e)$
7. For chromatic polynomial: $p_G = p_{G-e} - p_{G/e}$ (note the minus sign)
8. For Tutte polynomial: $T_G = T_{G-e} + T_{G/e}$ (plus sign)

# Construction / Recognition
## Deletion
1. Remove edge $e$ from the edge set
2. Keep all vertices

## Contraction
1. If $e$ joins $u$ and $v$: replace $u, v$ with a single vertex $w = (uv)$
2. Redirect all other edges incident to $u$ or $v$ to $w$ instead
3. Remove $e$ itself

# Context & Application
Deletion-contraction is the recursive engine behind the Tutte polynomial, chromatic polynomial, flow polynomial, and many other graph polynomials. "Similarly to the chromatic polynomial, the Tutte polynomial can be defined recursively by the cut and fuse operations" (p. 340). The operation extends naturally to multigraphs with loops.

# Examples
**Example** (Fig. X.1, p. 342): For $G$ with edge $e = uv$: $G - e$ removes $e$ keeping $u, v$ separate; $G/e$ merges $u$ and $v$ into one vertex.

**Example** (p. 156, Ch V): For non-adjacent vertices $a, b$: $p_G = p_{G+ab} + p_{G/ab}$.

# Relationships
## Enables
- **tutte-polynomial** — Defined via deletion-contraction
- **rank-generating-polynomial** — Satisfies analogous recursion
- **chromatic-polynomial** — Computed by $p_G = p_{G-e} - p_{G/e}$
- **flow-polynomial** — Also uses deletion-contraction

# Common Errors
- **Error**: Getting the sign wrong: chromatic uses minus ($p_G = p_{G-e} - p_{G/e}$) while Tutte uses plus ($T_G = T_{G-e} + T_{G/e}$).
  **Correction**: Always check which polynomial you are computing.

- **Error**: Contracting a loop and expecting a different graph from deletion.
  **Correction**: If $e$ is a loop, $G/e = G - e$.

# Common Confusions
- **Confusion**: Confusing the two formulations for chromatic polynomial (non-edge vs edge based).
  **Clarification**: For non-edge $ab$: $p_G = p_{G+ab} + p_{G/ab}$. For edge $e$: $p_G = p_{G-e} - p_{G/e}$.

# Source Reference
Chapter X, Section X.1, pages 341-342. Also Chapter V, Section V.1, pages 156-158.

# Verification Notes
- Definition source: Direct from p. 341 (Ch X) and p. 156 (Ch V)
- Confidence rationale: Explicit definition with figure
- Uncertainties: None
- Cross-reference status: Re-extracted from Ch X; Ch V content preserved
