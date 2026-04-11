---
concept: Short Exact Sequence
slug: short-exact-sequence
category: module-theory
subcategory: exact-sequences
tier: advanced
source: "Abstract Algebra"
source_slug: abs-alg
authors: "David S. Dummit, Richard M. Foote"
chapter: "Introduction to Module Theory"
chapter_number: 10
pdf_page: 388
section: "10.5 Exact Sequences"
extraction_confidence: high
aliases:
  - "s.e.s."
prerequisites:
  - exact-sequence
extends:
  - exact-sequence
related:
  - split-exact-sequence
  - extension-problem
contrasts_with: []
answers_questions:
  - "What is a short exact sequence?"
---

# Quick Definition
A short exact sequence $0 \to A \xrightarrow{\psi} B \xrightarrow{\varphi} C \to 0$ is exact, meaning $\psi$ is injective, $\varphi$ is surjective, and $\text{image}(\psi) = \ker(\varphi)$. Equivalently, B is an extension of C by A.

# Core Definition
The exact sequence $0 \to A \xrightarrow{\psi} B \xrightarrow{\varphi} C \to 0$ is called a short exact sequence. This holds iff $\psi$ is injective, $\varphi$ is surjective, and $\text{image}(\psi) = \ker(\varphi)$, i.e., B is an extension of C by A (Dummit & Foote, Corollary 23, p. 388).

# Prerequisites
- **exact-sequence** — A short exact sequence is a special type of exact sequence

# Key Properties
1. Encodes that B contains (a copy of) A with quotient B/A isomorphic to C
2. The extension problem: given A and C, determine all possible B
3. Any exact sequence can be broken into short exact sequences
4. A short exact sequence splits iff $B \cong A \oplus C$

# Examples
**Example 1** (p. 388): $0 \to A \xrightarrow{\iota} A \oplus C \xrightarrow{\pi} C \to 0$ is always a short exact sequence.
**Example 2** (p. 389): $0 \to \mathbb{Z} \xrightarrow{n} \mathbb{Z} \xrightarrow{\pi} \mathbb{Z}/n\mathbb{Z} \to 0$ is a non-split short exact sequence for $n \geq 2$.

# Relationships
## Builds Upon
- **exact-sequence**

## Enables
- **split-exact-sequence** — When B decomposes as a direct sum
- **projective-module** — Every s.e.s. ending in a projective module splits
- **injective-module** — Every s.e.s. beginning with an injective module splits

# Source Reference
Chapter 10, Section 10.5, pp. 388-391.

# Verification Notes
- Confidence: HIGH — explicit definition with examples
