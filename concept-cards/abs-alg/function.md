---
concept: Function
slug: function
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
  - "map"
  - "mapping"
prerequisites:
  - set
extends: []
related:
  - injection
  - surjection
  - bijection
  - permutation
contrasts_with: []
answers_questions:
  - "What is a function between sets?"
  - "What does it mean for a function to be well defined?"
---

# Quick Definition
A function (or map) $f: A \to B$ assigns to each element of the domain A a unique element of the codomain B. The notation $f: a \mapsto b$ indicates $f(a) = b$.

# Core Definition
The notation $f: A \to B$ or $A \xrightarrow{f} B$ denotes a function f from A to B with value f(a) at $a \in A$. The set A is the *domain* and B is the *codomain*. Functions are applied on the left. The image of f is $f(A) = \{b \in B \mid b = f(a) \text{ for some } a \in A\}$. The preimage of $C \subseteq B$ is $f^{-1}(C) = \{a \in A \mid f(a) \in C\}$. The fiber of f over b is the preimage of $\{b\}$. A function is *well defined* if it is unambiguously determined (Dummit & Foote, pp. 1-2).

# Prerequisites
- **Set** — Functions map between sets

# Key Properties
1. Each element of the domain maps to exactly one element of the codomain
2. The image $f(A)$ is a subset of B (equals B iff f is surjective)
3. $f^{-1}$ is not in general a function; fibers may contain many elements
4. Composition $(g \circ f)(a) = g(f(a))$ is defined when the codomain of f matches the domain of g
5. Well-definedness must be verified when a function is specified by a rule involving choices

# Construction / Recognition
## To Construct/Create:
1. Specify the domain A and codomain B
2. Give a rule assigning to each $a \in A$ a unique $f(a) \in B$
3. Verify well-definedness if the rule involves representatives

## To Identify/Recognize:
1. Check that every domain element has exactly one image
2. Check that every image lies in the codomain

# Context & Application
Functions are the fundamental connective tissue of algebra. Homomorphisms are structure-preserving functions between groups, and group actions are functions from $G \times A$ to A. The notion of well-definedness becomes critical when defining operations on equivalence classes or cosets.

# Examples
**Example 1** (p. 2): Trying to define $f: A_1 \cup A_2 \to \{0,1\}$ by mapping $A_1$ to 0 and $A_2$ to 1 fails unless $A_1 \cap A_2 = \emptyset$.

# Relationships
## Builds Upon
- **set** — Functions are defined between sets

## Enables
- **injection** — Injective functions
- **surjection** — Surjective functions
- **bijection** — Bijective functions
- **homomorphism** — Structure-preserving functions between groups

## Related
- **permutation** — A bijection from a set to itself

## Contrasts With
None.

# Common Errors
- **Error**: Forgetting to check well-definedness when defining functions on cosets or equivalence classes. **Correction**: Always verify the output does not depend on the choice of representative.

# Common Confusions
- **Confusion**: Confusing the image $f(A)$ with the codomain B. **Clarification**: The image is the subset of B actually hit by f; they are equal only when f is surjective.

# Source Reference
Chapter 0: Preliminaries, Section 0.1 "Basics," pages 1-3.

# Verification Notes
- Definition source: direct from source pp. 1-2
- Confidence rationale: explicitly defined with examples
- Uncertainties: none
- Cross-reference status: verified
