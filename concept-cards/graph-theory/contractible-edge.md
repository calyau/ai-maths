---
concept: Contractible Edge
slug: contractible-edge
category: connectivity
tier: intermediate
source: "Graph Theory"
source_slug: graph-theory
authors: "Reinhard Diestel"
chapter: "Connectivity"
chapter_number: 3
pdf_page: 68
section: "3.2 The structure of 3-connected graphs"
extraction_confidence: high
aliases:
  - "contractible edge in 3-connected graph"
prerequisites:
  - three-connected-graph
  - edge-contraction
extends: []
related:
  - tuttes-wheel-theorem
contrasts_with: []
answers_questions:
  - "What is a contractible edge in a 3-connected graph?"
---

# Quick Definition
In a 3-connected graph G, an edge e is contractible if G/e is again 3-connected. Every 3-connected graph with more than 4 vertices has such an edge.

# Core Definition
**Lemma 3.2.1.** If G is 3-connected and |G| > 4, then G has an edge e such that G/e is again 3-connected (Diestel, p. 68).

# Prerequisites
- **3-connected graph** — the context for contractible edges
- **Edge contraction** — the operation G/e

# Key Properties
1. G/e must remain 3-connected (kappa(G/e) >= 3)
2. Guaranteed to exist when |G| > 4
3. K4 (|G| = 4) has no contractible edge (contracting any edge gives K3, which is not 3-connected)
4. The proof is by contradiction using separators of size 2 in G/e
5. Foundation for Tutte's wheel theorem

# Construction / Recognition
## To Find a Contractible Edge (from the proof)
1. For each edge e = xy in G
2. Check if G/e is 3-connected
3. If so, e is contractible
4. Lemma 3.2.1 guarantees at least one exists (when |G| > 4)

# Context & Application
Contractible edges enable inductive proofs about 3-connected graphs. Lemma 3.2.1 is the foundation of Tutte's wheel theorem and the proof of Theorem 3.2.3 (cycle space generation).

# Examples
**Example** (p. 68, Fig. 3.2.1): The proof shows that if no edge is contractible, then for each edge xy there exists z such that {x, y, z} separates G. This leads to a contradiction by choosing edge xy, vertex z, and component C to minimize |C|.

# Relationships
## Builds Upon
- **3-connected graph**, **edge contraction**

## Enables
- **Tutte's wheel theorem** — uses contractible edges for the inductive step

# Common Errors
- **Error**: Expecting every edge in a 3-connected graph to be contractible
  **Correction**: Only some edges are contractible; the lemma guarantees at least one exists

# Source Reference
Chapter 3, Section 3.2, Lemma 3.2.1, p. 68 (pdf p. 68).

# Verification Notes
- Lemma from p. 68
- Confidence: HIGH — explicitly stated and proved
