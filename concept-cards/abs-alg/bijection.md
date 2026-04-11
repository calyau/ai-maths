---
concept: Bijection
slug: bijection
category: foundations
subcategory: set-theory
tier: foundational
source: "Abstract Algebra"
source_slug: abs-alg
authors: "David S. Dummit, Richard M. Foote"
chapter: "Preliminaries"
chapter_number: 0
pdf_page: 14
section: "0.1 Basics"
extraction_confidence: high
aliases:
  - "bijective function"
  - "one-to-one correspondence"
prerequisites:
  - function
extends:
  - function
related:
  - injection
  - surjection
  - permutation
  - isomorphism
contrasts_with: []
answers_questions:
  - "What is a bijection?"
  - "When does a function have a two-sided inverse?"
---

# Quick Definition
A function $f: A \to B$ is bijective if it is both injective (one-to-one) and surjective (onto). A bijection has a unique two-sided inverse.

# Core Definition
A function $f: A \to B$ is *bijective* or is a *bijection* if it is both injective and surjective. Equivalently, f is a bijection if and only if there exists a unique $g: B \to A$ such that $f \circ g$ is the identity on B and $g \circ f$ is the identity on A. This g is the *two-sided inverse* of f. For finite sets with $|A| = |B|$, bijectivity is equivalent to injectivity alone or surjectivity alone (Dummit & Foote, p. 2, Proposition 1).

# Prerequisites
- **Function** — Bijections are functions with special properties

# Key Properties
1. Bijection = injection + surjection
2. Has a unique two-sided inverse
3. For finite sets of equal cardinality: injective $\iff$ surjective $\iff$ bijective
4. A *permutation* of a set A is a bijection from A to itself

# Construction / Recognition
## To Identify/Recognize:
1. Show f is both injective and surjective, OR
2. Construct a two-sided inverse

# Context & Application
Bijections establish that two sets have the same cardinality. In group theory, isomorphisms are bijective homomorphisms, and permutations (elements of symmetric groups) are bijections.

# Examples
**Example 1** (p. 2): The exponential map $\exp: \mathbb{R} \to \mathbb{R}^+$ is a bijection with inverse $\log_e$.

# Relationships
## Builds Upon
- **function** — A bijection is a function

## Enables
- **permutation** — A bijection from a set to itself
- **isomorphism** — A bijective homomorphism

## Related
- **injection** — One component of bijectivity
- **surjection** — The other component

## Contrasts With
None.

# Common Errors
- **Error**: Assuming a one-sided inverse makes a function bijective. **Correction**: A left inverse proves injectivity; a right inverse proves surjectivity. Both are needed in general.

# Common Confusions
- **Confusion**: Thinking every function has an inverse function. **Clarification**: Only bijections have two-sided inverses; $f^{-1}(C)$ as a preimage of a set is always defined.

# Source Reference
Chapter 0: Preliminaries, Section 0.1 "Basics," page 2, Proposition 1.

# Verification Notes
- Definition source: direct from source p. 2
- Confidence rationale: explicitly defined
- Uncertainties: none
- Cross-reference status: verified
