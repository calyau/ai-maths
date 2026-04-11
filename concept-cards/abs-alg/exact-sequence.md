---
concept: Exact Sequence
slug: exact-sequence
category: module-theory
subcategory: exact-sequences
tier: advanced
source: "Abstract Algebra"
source_slug: abs-alg
authors: "David S. Dummit, Richard M. Foote"
chapter: "Introduction to Module Theory"
chapter_number: 10
pdf_page: 387
section: "10.5 Exact Sequences"
extraction_confidence: high
aliases: []
prerequisites:
  - module-homomorphism
  - submodule
extends: []
related:
  - short-exact-sequence
  - split-exact-sequence
  - projective-module
  - injective-module
contrasts_with: []
answers_questions:
  - "What is an exact sequence?"
---

# Quick Definition
A sequence of module homomorphisms $\cdots \to X_{n-1} \xrightarrow{\alpha} X_n \xrightarrow{\beta} X_{n+1} \to \cdots$ is exact at $X_n$ if $\text{image}(\alpha) = \ker(\beta)$. The sequence is exact if it is exact at every module between a pair of homomorphisms.

# Core Definition
The pair of homomorphisms $X \xrightarrow{\alpha} Y \xrightarrow{\beta} Z$ is said to be exact (at Y) if $\text{image}(\alpha) = \ker(\beta)$. A sequence $\cdots \to X_{n-1} \to X_n \to X_{n+1} \to \cdots$ of homomorphisms is an exact sequence if it is exact at every $X_n$ between a pair of homomorphisms (Dummit & Foote, p. 387).

# Prerequisites
- **module-homomorphism** — Exact sequences consist of homomorphisms
- **submodule** — Kernels and images are submodules

# Key Properties
1. $0 \to A \xrightarrow{\psi} B$ is exact iff $\psi$ is injective
2. $B \xrightarrow{\varphi} C \to 0$ is exact iff $\varphi$ is surjective
3. Any exact sequence can be decomposed into short exact sequences
4. Exactness is the fundamental condition in homological algebra

# Context & Application
Exact sequences capture the relationship between submodules, modules, and quotient modules. They are the language of homological algebra and essential for understanding module structure.

# Examples
**Example** (p. 388): For any homomorphism $\varphi: B \to C$, the sequence $0 \to \ker\varphi \xrightarrow{\iota} B \xrightarrow{\varphi} \text{image}(\varphi) \to 0$ is exact.

# Relationships
## Builds Upon
- **module-homomorphism**

## Enables
- **short-exact-sequence** — The most important special case
- **projective-module**, **injective-module**, **flat-module** — Defined by exactness preservation

# Source Reference
Chapter 10, Section 10.5, pp. 387-389.

# Verification Notes
- Definition: direct from p. 387
- Confidence: HIGH — explicit definition
