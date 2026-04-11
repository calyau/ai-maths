---
concept: Split Exact Sequence
slug: split-exact-sequence
category: module-theory
subcategory: exact-sequences
tier: advanced
source: "Abstract Algebra"
source_slug: abs-alg
authors: "David S. Dummit, Richard M. Foote"
chapter: "Introduction to Module Theory"
chapter_number: 10
pdf_page: 393
section: "10.5 Exact Sequences"
extraction_confidence: high
aliases:
  - "split extension"
prerequisites:
  - short-exact-sequence
  - direct-sum-of-modules
extends:
  - short-exact-sequence
related:
  - projective-module
  - splitting-homomorphism
contrasts_with: []
answers_questions:
  - "When does a short exact sequence split?"
---

# Quick Definition
A short exact sequence $0 \to A \xrightarrow{\psi} B \xrightarrow{\varphi} C \to 0$ of R-modules is split if there is an R-module complement to $\psi(A)$ in B, equivalently if $B \cong A \oplus C$.

# Core Definition
The short exact sequence $0 \to A \xrightarrow{\psi} B \xrightarrow{\varphi} C \to 0$ is split if there is an R-module complement to $\psi(A)$ in B. Equivalently, there exists a splitting homomorphism $\mu: C \to B$ with $\varphi \circ \mu = \text{id}_C$. Also equivalently, there exists $\lambda: B \to A$ with $\lambda \circ \psi = \text{id}_A$. In the split case, $B = \psi(A) \oplus C'$ where $C' \cong C$ (Dummit & Foote, Propositions 25-26, pp. 393-395).

# Prerequisites
- **short-exact-sequence** — Splitting is a property of short exact sequences
- **direct-sum-of-modules** — A split s.e.s. gives a direct sum

# Key Properties
1. Three equivalent conditions: complement exists; right splitting $\mu$ exists; left splitting $\lambda$ exists
2. If the sequence splits, $B \cong A \oplus C$
3. Every s.e.s. ending in a projective module splits
4. Every s.e.s. beginning with an injective module splits
5. For groups, a split extension gives a semidirect product (not necessarily direct)

# Examples
**Example 1** (p. 394): $0 \to \mathbb{Z} \to \mathbb{Z} \oplus \mathbb{Z}/n\mathbb{Z} \to \mathbb{Z}/n\mathbb{Z} \to 0$ is split.
**Example 2** (p. 394): $0 \to \mathbb{Z} \xrightarrow{n} \mathbb{Z} \to \mathbb{Z}/n\mathbb{Z} \to 0$ is NOT split (no nonzero map from $\mathbb{Z}/n\mathbb{Z}$ to $\mathbb{Z}$).

# Relationships
## Builds Upon
- **short-exact-sequence**, **direct-sum-of-modules**

## Related
- **projective-module** — P is projective iff every s.e.s. onto P splits
- **injective-module** — Q is injective iff every s.e.s. from Q splits

# Source Reference
Chapter 10, Section 10.5, pp. 393-396.

# Verification Notes
- Confidence: HIGH — explicit propositions with three equivalent characterizations
