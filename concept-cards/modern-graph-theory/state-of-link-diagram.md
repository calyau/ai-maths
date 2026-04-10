---
concept: State of a Link Diagram
slug: state-of-link-diagram
category: knot-theory
subcategory: null
tier: advanced
source: "Modern Graph Theory"
source_slug: modern-graph-theory
authors: "Béla Bollobás"
chapter: "The Tutte Polynomial"
chapter_number: 10
pdf_page: 368
section: "X.6 Polynomials of Knots and Links"
extraction_confidence: high
aliases:
  - "splitting"
  - "state S"
prerequisites:
  - link-diagram
extends: []
related:
  - kauffman-square-bracket
  - kauffman-bracket
contrasts_with: []
answers_questions:
  - "How do knot polynomials relate to the Tutte polynomial?"
---

# Quick Definition
A state $S$ of a link diagram with $n$ crossings is a choice of slicing (A-slice or B-slice) for each crossing, giving $2^n$ states. Each state produces a splitting: a collection of unlinked trivial knots.

# Core Definition
"A state $S$ of a link diagram is a choice of slicing for each crossing of the diagram; thus a diagram with $n$ crossings has $2^n$ states" (Bollobás, p. 368). Writing $V$ for the set of crossings, $S: V \to \{A, B\}$. The state has $a_L(S)$ A-slices, $b_L(S)$ B-slices, and the splitting has $c_L(S)$ components.

# Prerequisites
- **Link diagram** — States are defined on link diagrams

# Key Properties
1. $2^n$ states for $n$ crossings
2. Each state gives a splitting into $c_L(S)$ disjoint simple closed curves
3. $a_L(S) + b_L(S) = n$ (total number of crossings)
4. The Kauffman square bracket sums over all states

# Examples
**Example** (Fig. X.10, p. 368): A state of the figure-of-eight knot with $a = 3$, $b = 1$, $c = 2$.

# Relationships
## Builds Upon
- **link-diagram**

## Enables
- **kauffman-square-bracket** — $[L] = \sum_S A^{a(S)} B^{b(S)} d^{c(S)-1}$
- **kauffman-bracket** — Evaluation of the square bracket

# Source Reference
Chapter X, Section X.6, page 368. Figure X.10.

# Verification Notes
- Definition source: Direct from p. 368
- Confidence rationale: Explicit definition
- Uncertainties: None
- Cross-reference status: Verified
