---
concept: Existence of Maximal Ideals
slug: maximal-ideal-existence
category: ring-theory
subcategory: structure-theorems
tier: intermediate
source: "Abstract Algebra"
source_slug: abs-alg
authors: "David S. Dummit, Richard M. Foote"
chapter: "Introduction to Rings"
chapter_number: 7
pdf_page: 254
section: "7.4 Properties of Ideals"
extraction_confidence: high
aliases:
  - "Krull's theorem"
prerequisites:
  - ring-with-identity
  - maximal-ideal
extends: []
related:
  - maximal-ideal
contrasts_with: []
answers_questions:
  - "Does every ring have a maximal ideal?"
---

# Quick Definition
In a ring with identity $1 \neq 0$, every proper ideal is contained in a maximal ideal. This is proved using Zorn's Lemma.

# Core Definition
(Proposition 11) In a ring with identity, every proper ideal is contained in a maximal ideal. The proof uses Zorn's Lemma: the set of proper ideals containing a given proper ideal I is nonempty and every chain has an upper bound (their union, which is proper since $1$ is not in any ideal in the chain) (Dummit & Foote, pp. 254-255).

# Prerequisites
- **Ring with identity** — Need $1 \neq 0$
- **Maximal ideal** — The conclusion involves maximal ideals

# Key Properties
1. Requires Zorn's Lemma (a form of the Axiom of Choice)
2. A ring without identity may have no maximal ideals
3. Combined with Proposition 12: every commutative ring with $1 \neq 0$ has a quotient that is a field

# Source Reference
Chapter 7, Section 7.4, Proposition 11, pages 254-255.

# Verification Notes
- Definition: Direct from Proposition 11, pp. 254-255
- Confidence: HIGH — explicit proposition with proof
