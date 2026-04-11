---
concept: Injective Module
slug: injective-module
category: module-theory
subcategory: exact-sequences
tier: advanced
source: "Abstract Algebra"
source_slug: abs-alg
authors: "David S. Dummit, Richard M. Foote"
chapter: "Introduction to Module Theory"
chapter_number: 10
pdf_page: 406
section: "10.5 Exact Sequences"
extraction_confidence: high
aliases: []
prerequisites:
  - short-exact-sequence
  - module-homomorphism
extends: []
related:
  - projective-module
  - flat-module
  - baers-criterion
  - divisible-module
contrasts_with:
  - projective-module
answers_questions:
  - "What is an injective module?"
---

# Quick Definition
An R-module Q is injective if every short exact sequence $0 \to Q \to M \to N \to 0$ splits, or equivalently, if every homomorphism from a submodule of M into Q extends to all of M.

# Core Definition
An R-module Q is called injective if it satisfies any of these equivalent conditions (Proposition 34): (1) $\text{Hom}_R(\_, Q)$ takes short exact sequences to short exact sequences; (2) Every injection from Q can be extended: given $\psi: L \hookrightarrow M$ and $f: L \to Q$, there exists $F: M \to Q$ with $F \circ \psi = f$; (3) Every short exact sequence $0 \to Q \to M \to N \to 0$ splits (Dummit & Foote, Proposition 34, pp. 406-407).

# Prerequisites
- **short-exact-sequence** — Injectivity is characterized by splitting
- **module-homomorphism** — The extension property uses homomorphisms

# Key Properties
1. $\text{Hom}_R(\_, Q)$ is exact iff Q is injective
2. Every R-module is contained in an injective R-module (Theorem 38)
3. A $\mathbb{Z}$-module is injective iff it is divisible (Proposition 36)
4. Over a PID, Q is injective iff $rQ = Q$ for every nonzero $r \in R$
5. Quotients of injective modules over PIDs are injective
6. Direct sums of injective modules are injective

# Context & Application
Injective modules are dual to projective modules. While every module is a quotient of a projective module, every module embeds in an injective module. This duality is fundamental to homological algebra.

# Examples
**Example 1** (p. 409): $\mathbb{Q}$ is an injective $\mathbb{Z}$-module (it is divisible).
**Example 2** (p. 409): $\mathbb{Q}/\mathbb{Z}$ is an injective $\mathbb{Z}$-module.
**Example 3** (p. 409): $\mathbb{Z}$ is NOT injective as a $\mathbb{Z}$-module (not divisible).

# Relationships
## Builds Upon
- **short-exact-sequence**

## Related
- **baers-criterion** — Characterizes injectivity by extending maps from ideals
- **divisible-module** — Over a PID, injective = divisible

## Contrasts With
- **projective-module** — Dual notion; projective lifts, injective extends

# Source Reference
Chapter 10, Section 10.5, Proposition 34, pp. 406-410. See also Proposition 36 (Baer's Criterion).

# Verification Notes
- Confidence: HIGH — explicit definition with three equivalent characterizations
