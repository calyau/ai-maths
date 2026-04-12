---
# === CORE IDENTIFICATION ===
concept: Free Abelian Group
slug: free-abelian-group

# === CLASSIFICATION ===
category: abelian-groups
subcategory: null
tier: advanced

# === PROVENANCE ===
source: "Groups and Symmetry"
source_slug: groups-symmetry
authors: "M.A. Armstrong"
chapter: "Finitely Generated Abelian Groups"
chapter_number: 21
pdf_page: 126
section: "Corollary 21.3"

# === CONFIDENCE ===
extraction_confidence: high

# === VARIANTS (authority control) ===
aliases: []

# === TYPED RELATIONSHIPS ===
prerequisites:
  - classification-of-fg-abelian-groups
extends:
  - finitely-generated-abelian-group
related:
  - rank-of-abelian-group
  - smith-normal-form
contrasts_with: []

# === COMPETENCY QUESTIONS ===
answers_questions:
  - "What is a free abelian group?"
  - "When is a finitely generated abelian group free?"
---

# Quick Definition

A free abelian group of rank $s$ is a group isomorphic to $\mathbb{Z}^s$, the direct product of $s$ copies of $\mathbb{Z}$. It is a finitely generated abelian group with no elements of finite order.

# Core Definition

**(21.3) Corollary.** Any finitely generated abelian group in which there are no elements of finite order is isomorphic to the direct product of a finite number of copies of $\mathbb{Z}$. A group which is isomorphic to the direct product of $s$ copies of $\mathbb{Z}$ is called a **free abelian group** of rank $s$ (Armstrong, p. 126).

# Prerequisites

- **Classification of f.g. abelian groups** -- the free abelian case is the special case with no torsion

# Key Properties

1. Elements are integer-coefficient linear combinations $n_1 x_1 + \cdots + n_s x_s$
2. No non-trivial relations: the only way $n_1 x_1 + \cdots + n_s x_s = 0$ is $n_1 = \cdots = n_s = 0$
3. $\mathbb{Z}^s \cong \mathbb{Z}^t$ iff $s = t$ (Lemma 21.7)
4. Every subgroup of a free abelian group of rank $s$ is free abelian of rank $\le s$

# Construction / Recognition

## To Recognize a Free Abelian Group:
1. Check that the group is abelian and finitely generated
2. Check that no non-identity element has finite order
3. If both hold, the group is free abelian

## From Generators and Relations:
If the Smith normal form of the relation matrix has no non-zero diagonal entries (or the matrix is zero), the group is free abelian. The rank equals $n - \text{rank}(A)$ where $n$ is the number of generators and $\text{rank}(A)$ is the number of non-zero diagonal entries.

# Context & Application

Free abelian groups serve as the "base" from which all finitely generated abelian groups are constructed via quotients. In Chapter 21, Armstrong writes the canonical form as a quotient $A/N$ where $A$ is free abelian and $N$ encodes the relations.

# Examples

$\mathbb{Z}^2 = \mathbb{Z} \times \mathbb{Z}$ is the free abelian group of rank 2 (the integer lattice in the plane).

**Exercise 22.3** (p. 136): The group determined by four generators and three relations with a relation matrix of full column rank turns out to be free abelian of rank 1.

# Relationships

## Builds Upon
- **Classification of f.g. abelian groups** -- the free case is $k = 0$ in the classification

## Related
- **Rank** -- the rank of a free abelian group equals the number of copies of $\mathbb{Z}$
- **Smith normal form** -- used to check if a group is free abelian

# Common Confusions

- **Confusion**: Thinking "free abelian" means "free group that is abelian."
  **Clarification**: A free group on $s \ge 2$ generators is non-abelian. A free abelian group of rank $s$ is $\mathbb{Z}^s$, which is abelian by definition.

# Source Reference

Chapter 21: Finitely Generated Abelian Groups, Corollary 21.3, page 126.

# Verification Notes

- Definition: Direct from Corollary 21.3, p. 126
- Confidence: HIGH -- explicitly defined
