---
# === CORE IDENTIFICATION ===
concept: Free Group
slug: free-group

# === CLASSIFICATION ===
category: free-groups-presentations
subcategory: null
tier: foundational

# === PROVENANCE ===
source: "Group Theory"
source_slug: group-theory
authors: "J.S. Milne"
chapter: "Free Groups and Presentations; Coxeter Groups"
chapter_number: 2
pdf_page: 31
section: "Free groups"

# === CONFIDENCE ===
extraction_confidence: high

# === VARIANTS (authority control) ===
aliases:
  - "F_X"

# === TYPED RELATIONSHIPS ===
prerequisites:
  - word
  - reduced-word
  - free-monoid
extends: []
related:
  - universal-property-free-groups
  - rank-of-free-group
  - group-presentation
contrasts_with:
  - finitely-presented-group

# === COMPETENCY QUESTIONS ===
answers_questions:
  - "What is a free group?"
  - "What distinguishes a free group from a finitely presented group?"
  - "How are free groups constructed?"
---

# Quick Definition

The free group $F_X$ on a set $X$ is a group whose elements are equivalence classes of words in $X' = \{a, a^{-1}, b, b^{-1}, \ldots\}$, where two words are equivalent iff they have the same reduced form. There are no relations except those implied by the group axioms.

# Core Definition

"Let $F_X$ be the set of equivalence classes of words. Proposition 2.2 shows that the binary operation on $W'$ defines a binary operation on $F_X$, which obviously makes it into a monoid. It also has inverses... Thus $F_X$ is a group, called the **free group** on $X$." (Milne, p. 32)

"The elements of $F_X$ are represented by words in $X'$; two words represent the same element of $F_X$ if and only if they have the same reduced forms; multiplication is defined by juxtaposition; the empty word represents 1; inverses are obtained in the obvious way." (p. 33)

# Prerequisites

- **Word** — elements are represented by words
- **Reduced word** — each element has a unique reduced representative
- **Free monoid** — the free group extends the free monoid construction

# Key Properties

1. Each element is represented by a unique reduced word
2. Multiplication: juxtapose words and reduce
3. $X$ generates $F_X$
4. Universal property: any map $X \to G$ extends uniquely to a homomorphism $F_X \to G$ (Proposition 2.3)
5. The free group on $\{a\}$ is $C_\infty$ (infinite cyclic)
6. The free group on two or more generators is already very complicated
7. Every group is a quotient of a free group (Corollary 2.5)

# Construction / Recognition

## Construction:
1. Form $X' = \{a, a^{-1}, b, b^{-1}, \ldots\}$
2. Take all words on $X'$
3. Define equivalence: $w \sim w'$ iff same reduced form
4. Multiplication: juxtapose representatives, then reduce
5. Identity: empty word; inverse: reverse word with inverted symbols

# Context & Application

Free groups are the "most general" groups on a given set of generators -- they satisfy no relations beyond the group axioms. Every group is a quotient of a free group, making free groups the starting point for group presentations.

# Examples

**Example 1** (p. 33): The free group on $\{a\}$ is $C_\infty = \{\ldots, a^{-2}, a^{-1}, 1, a, a^2, \ldots\}$.

**Example 2** (p. 33): The free group on $\{a, b\}$ is very complicated -- its commutator subgroup has infinite rank (footnote 2).

**Example 3** (p. 33): Corollary 2.5 -- every group $G$ is a quotient of a free group (choose $X = G$ as generators).

# Relationships

## Builds Upon
- **word**, **reduced-word**, **free-monoid**

## Enables
- **group-presentation** — groups are presented as quotients of free groups
- **universal-property-free-groups** — characterizes $F_X$
- **nielsen-schreier-theorem** — subgroups of free groups are free

## Contrasts With
- **finitely-presented-group** — a free group has no relations; a presented group has defining relations

# Common Errors

- **Error**: Thinking the free group on two generators is "simple" or abelian
  **Correction**: $F_2$ is extremely complex; its commutator subgroup has infinite rank

# Common Confusions

- **Confusion**: Confusing "free group" with "free abelian group"
  **Clarification**: The free abelian group on $\{a, b\}$ is $\mathbb{Z}^2$; the free group $F_{\{a,b\}}$ is nonabelian and much larger

# Source Reference

Chapter 2, Section "Free groups", pages 31-34. Propositions 2.1-2.3, Corollary 2.5.

# Verification Notes

- Definition source: Direct from p. 32-33
- Confidence: HIGH — explicit construction
- Uncertainties: None
