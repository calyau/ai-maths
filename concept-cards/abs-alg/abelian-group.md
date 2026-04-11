---
concept: Abelian Group
slug: abelian-group
category: group-theory
subcategory: basic-axioms
tier: foundational
source: "Abstract Algebra"
source_slug: abs-alg
authors: "David S. Dummit, Richard M. Foote"
chapter: "Introduction to Groups"
chapter_number: 1
pdf_page: 26
section: "1.1 Basic Axioms and Examples"
extraction_confidence: high
aliases:
  - "commutative group"
prerequisites:
  - group
extends:
  - group
related:
  - cyclic-group
  - center-of-a-group
contrasts_with:
  - dihedral-group
  - symmetric-group
answers_questions:
  - "What is an abelian group?"
  - "What special properties do abelian groups have?"
---

# Quick Definition
A group G is abelian (or commutative) if $ab = ba$ for all $a, b \in G$. Equivalently, $G = Z(G)$.

# Core Definition
The group $(G, \star)$ is *abelian* (or *commutative*) if $a \star b = b \star a$ for all $a, b \in G$ (Dummit & Foote, p. 18).

# Prerequisites
- **Group** — abelian groups are groups with extra commutativity

# Key Properties
1. Every subgroup of an abelian group is normal
2. Every cyclic group is abelian
3. Abelian groups have abelian quotients
4. $G$ is abelian iff $Z(G) = G$
5. If $G/Z(G)$ is cyclic then G is abelian
6. Every finite abelian group has a subgroup of order n for each divisor n of $|G|$

# Context & Application
Abelian groups are the "easy" case in group theory. Many results that are difficult for general groups become straightforward for abelian groups. Every finite abelian group decomposes as a direct product of cyclic groups (Fundamental Theorem of Finite Abelian Groups).

# Examples
**Example 1** (p. 18): $\mathbb{Z}, \mathbb{Q}, \mathbb{R}, \mathbb{C}$ under addition.
**Example 2** (p. 18): $\mathbb{Z}/n\mathbb{Z}$ under addition; $(\mathbb{Z}/n\mathbb{Z})^\times$ under multiplication.

# Relationships
## Builds Upon
- **group**

## Enables
- **cyclic-group** — all cyclic groups are abelian

## Related
- **center-of-a-group** — $G$ abelian iff $Z(G) = G$

## Contrasts With
- **dihedral-group** — non-abelian for $n \geq 3$
- **symmetric-group** — non-abelian for $n \geq 3$

# Source Reference
Chapter 1, Section 1.1, page 18.

# Verification Notes
- Definition source: direct from source p. 18
- Confidence rationale: explicitly defined
- Uncertainties: none
- Cross-reference status: verified
