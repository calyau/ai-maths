---
# === CORE IDENTIFICATION ===
concept: Linear Character
slug: linear-character

# === CLASSIFICATION ===
category: character-theory
subcategory: null
tier: advanced

# === PROVENANCE ===
source: "Group Theory"
source_slug: group-theory
authors: "J.S. Milne"
chapter: "Representations of Finite Groups"
chapter_number: 7
pdf_page: 114
section: "The characters of G"

# === CONFIDENCE ===
extraction_confidence: high

# === VARIANTS ===
aliases:
  - "degree-1 character"
  - "multiplicative character"

# === TYPED RELATIONSHIPS ===
prerequisites:
  - character-of-a-representation
  - one-dimensional-representation
extends:
  - irreducible-character
related:
  - representations-of-abelian-groups
  - principal-character
  - kernel-of-a-character
contrasts_with: []

# === COMPETENCY QUESTIONS ===
answers_questions:
  - "What is a linear character?"
  - "When is a character a group homomorphism?"
  - "What is a character of a commutative group?"
---

# Quick Definition

A character chi_V is linear if dim V = 1. In this case GL(V) = F^x, and chi_V(g) = rho(g) is a homomorphism G -> F^x.

# Core Definition

When V has dimension 1, the character chi_V of rho is said to be **linear**. In this case GL(V) = F^x, and so chi_V(g) = rho(g). Therefore chi_V is a homomorphism G -> F^x. This agrees with the earlier definition of linear character as a homomorphism G -> mu(C) (Chapter 1, p. 27). (Milne, Chapter 7, p. 114; Chapter 1, p. 27)

# Prerequisites

- **Character of a representation** — linear characters are a special case
- **One-dimensional representation** — the underlying representation has degree 1

# Key Properties

1. chi_V: G -> F^x is a group homomorphism
2. chi_V is both a character and a representation
3. The kernel of a linear character is a normal subgroup of G
4. The commutator subgroup G' is the intersection of the kernels of all linear characters (p. 119)
5. Number of linear characters = [G : G'] = |G/G'|
6. For abelian groups, all irreducible characters are linear
7. For a finite group, chi(g) is always a root of unity (|chi(g)| = 1)

# Construction / Recognition

1. A 1-dimensional representation rho: G -> F^x
2. Its character is chi(g) = rho(g) (trace of a 1x1 matrix)
3. This is a group homomorphism G -> F^x
4. Equivalently, a homomorphism G -> mu(C) (p. 27)

# Context & Application

Linear characters were first introduced for commutative groups (Chapter 1, p. 27), where the set of all characters forms the dual group G^v. In Chapter 7, linear characters are recognized as the special case of irreducible characters with degree 1. The number of linear characters equals [G : G'], providing a count that is useful in constructing character tables.

# Examples

**Example 1** (p. 27): The Legendre symbol (a/p): (Z/pZ)^x -> {+/-1} is a linear character.

**Example 2** (p. 117, 7.54): The sign character chi_1 of S_3 sends a permutation to its sign (+1 or -1). It is linear.

**Example 3** (p. 119): The commutator subgroup G' = intersection of kernels of all linear characters.

# Relationships

## Builds Upon
- **character-of-a-representation** — special case
- **one-dimensional-representation** — the underlying representation

## Enables
- Detection of the commutator subgroup: G' = intersection of kernels of linear characters
- **dual-group** — for abelian groups, the set of linear characters forms G^v

## Related
- **representations-of-abelian-groups** — all irreducible reps of abelian groups are 1-dimensional
- **principal-character** — the trivial linear character
- **orthogonality-relations** — linear characters satisfy orthogonality

# Common Errors

- **Error**: Thinking linear characters exist only for abelian groups
  **Correction**: Every group has linear characters (at least the trivial one); the number is [G : G']

# Common Confusions

- **Confusion**: Confusing "linear character" (degree 1) with "character" (trace of any representation)
  **Clarification**: In Chapter 1, "character" meant "linear character" (for abelian groups). In Chapter 7, "character" means the trace function of any representation, and "linear character" specifically means degree 1.

# Source Reference

Chapter 7: Representations of Finite Groups, p. 114. See also Chapter 1, p. 27 for the abelian case.

# Verification Notes

- Definition source: Direct from p. 114 (Chapter 7) and p. 27 (Chapter 1)
- Confidence rationale: HIGH — explicit definition
- Uncertainties: None
