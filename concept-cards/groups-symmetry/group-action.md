---
# === CORE IDENTIFICATION ===
concept: Group Action
slug: group-action

# === CLASSIFICATION ===
category: group-actions
subcategory: null
tier: advanced

# === PROVENANCE ===
source: "Groups and Symmetry"
source_slug: groups-symmetry
authors: "M.A. Armstrong"
chapter: "Actions, Orbits, and Stabilizers"
chapter_number: 17
pdf_page: 98
section: null

# === CONFIDENCE ===
extraction_confidence: high

# === VARIANTS (authority control) ===
aliases:
  - "G-action"
  - "group action on a set"
  - "permutation representation"

# === TYPED RELATIONSHIPS ===
prerequisites:
  - homomorphism
  - symmetric-group
extends: []
related:
  - orbit
  - stabilizer
  - transitive-action
  - conjugation-action
contrasts_with:
  - free-action

# === COMPETENCY QUESTIONS ===
answers_questions:
  - "What is a group action?"
  - "How does a group act on a set?"
  - "What distinguishes a group action from a group acting freely?"
---

# Quick Definition

An action of a group $G$ on a set $X$ is a homomorphism from $G$ to $S_X$, the symmetric group of all permutations of $X$. The elements of $G$ permute the points of $X$ in a way compatible with the group operation.

# Core Definition

An action of a group $G$ on a set $X$ is a homomorphism $\varphi \colon G \to S_X$. For each $g \in G$, the map $\varphi$ gives a permutation $\varphi(g)$ of $X$. Writing $g(x)$ for the image of $x$ under $\varphi(g)$, the homomorphism condition becomes $gh(x) = g(h(x))$ for any $g, h \in G$ and any $x \in X$ (Armstrong, p. 98).

Armstrong emphasises the word "an" in the definition: a given group may act on the same set in different ways.

# Prerequisites

- **Homomorphism** -- The definition of group action is literally a homomorphism into a symmetric group
- **Symmetric group** -- The target of the homomorphism $\varphi$ is $S_X$, the group of all permutations of $X$

# Key Properties

1. The identity element $e \in G$ acts as the identity permutation: $e(x) = x$ for all $x \in X$
2. The action is compatible with group multiplication: $gh(x) = g(h(x))$
3. Each group element acts as a bijection on $X$
4. A group may have multiple distinct actions on the same set
5. The kernel of the homomorphism $\varphi$ consists of elements that fix every point of $X$

# Construction / Recognition

## To Construct a Group Action:
1. Choose a group $G$ and a set $X$
2. Define, for each $g \in G$, a permutation of $X$
3. Verify the identity element acts as the identity permutation
4. Verify $gh(x) = g(h(x))$ for all $g, h \in G$ and $x \in X$

## To Recognize a Group Action:
1. Identify the group $G$ and the set $X$
2. Confirm each group element induces a well-defined permutation of $X$
3. Check the compatibility condition $gh(x) = g(h(x))$

# Context & Application

Group actions are a central organising concept in group theory. Armstrong describes the definition as having "all the qualities" of a good definition: precise, economical, capturing a simple intuitive idea, and easy to work with (p. 98). Actions provide the framework for studying symmetry, and many fundamental theorems (Orbit-Stabilizer, Counting Theorem, Sylow theorems) rely on them.

# Examples

**Example (i)** (p. 98): The infinite cyclic group $\mathbb{Z}$ acts on $\mathbb{R}$ by translation: $n$ sends $x$ to $n + x$. This is an action because $(m + n) + x = m + (n + x)$.

**Example (ii)** (p. 98): A second action of $\mathbb{Z}$ on $\mathbb{R}$: $n$ sends $x$ to $(-1)^n x$. Even integers act as the identity, odd integers as $x \mapsto -x$.

**Example (iii)** (p. 99): $\mathbb{Z}_4$ acts on the set of edges of a cube via rotation about an axis through opposite face centres.

**Example (iv)** (p. 99): $SO_3$ acts on the unit sphere in $\mathbb{R}^3$ by orthogonal transformations.

**Example (v)** (p. 100): Any group $G$ acts on itself by conjugation: $g$ sends $x$ to $gxg^{-1}$.

# Relationships

## Builds Upon
- **Homomorphism** -- a group action is defined as a homomorphism
- **Symmetric group** -- the codomain of the action homomorphism

## Enables
- **Orbit** -- the set of images of a point under all group elements
- **Stabilizer** -- the subgroup fixing a given point
- **Orbit-Stabilizer theorem** -- relates orbit size to stabilizer index
- **Counting theorem** -- counts orbits using fixed-point data

## Related
- **Transitive action** -- an action with a single orbit
- **Conjugation action** -- the canonical action of a group on itself
- **Product action** -- action of $G \times H$ on $X \times Y$
- **Diagonal action** -- action of $G$ on $X \times Y$ via $g(x, y) = (g(x), g(y))$

## Contrasts With
- **Free action** -- an action where only the identity has fixed points

# Common Errors

- **Error**: Forgetting to verify the compatibility condition $gh(x) = g(h(x))$ when constructing an action.
  **Correction**: Both conditions (identity acts trivially, and compatibility) must be checked. The compatibility condition is equivalent to requiring $\varphi$ to be a homomorphism.

- **Error**: Confusing left and right actions by writing $g(h(x))$ when meaning $(gh)(x)$.
  **Correction**: The convention $gh(x) = g(h(x))$ defines a left action. Be consistent.

# Common Confusions

- **Confusion**: Thinking a group can act on a set in only one way.
  **Clarification**: Armstrong explicitly notes (Example (ii)) that the same group $\mathbb{Z}$ can act on the same set $\mathbb{R}$ in entirely different ways.

- **Confusion**: Believing every group action must be faithful (injective homomorphism).
  **Clarification**: The kernel of the action homomorphism may be non-trivial; elements in the kernel act as the identity permutation.

# Source Reference

Chapter 17: Actions, Orbits, and Stabilizers, pages 98-100. Definition at top of p. 98, Examples (i)--(v) on pp. 98--100.

# Verification Notes

- Definition: Direct from first paragraph of Chapter 17 (p. 98)
- Examples: All taken directly from source
- Confidence: HIGH -- explicit, clearly stated definition
- Cross-references: All slug references verified against planned extractions
