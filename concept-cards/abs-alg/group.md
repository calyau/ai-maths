---
concept: Group
slug: group
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
  - "abstract group"
prerequisites:
  - binary-operation
extends:
  - binary-operation
related:
  - abelian-group
  - subgroup
  - homomorphism
  - order-of-a-group
contrasts_with:
  - monoid
answers_questions:
  - "What is a group?"
  - "What are the group axioms?"
  - "What distinguishes a group from a monoid?"
  - "What is a finite group?"
---

# Quick Definition
A group is an ordered pair $(G, \star)$ where G is a set and $\star$ is an associative binary operation on G with an identity element and inverses for every element. A group is abelian if the operation is commutative.

# Core Definition
A *group* is an ordered pair $(G, \star)$ where G is a set and $\star$ is a binary operation on G satisfying: (i) *associativity*: $(a \star b) \star c = a \star (b \star c)$ for all $a, b, c \in G$; (ii) *identity*: there exists $e \in G$ such that $a \star e = e \star a = a$ for all $a \in G$; (iii) *inverses*: for each $a \in G$ there exists $a^{-1} \in G$ such that $a \star a^{-1} = a^{-1} \star a = e$. The group is *abelian* (or commutative) if $a \star b = b \star a$ for all $a, b \in G$. A *finite group* is a group whose underlying set is finite (Dummit & Foote, pp. 17-18).

# Prerequisites
- **Binary operation** — a group requires an associative binary operation

# Key Properties
1. The identity is unique (Proposition 1.1)
2. Inverses are unique: for each a, $a^{-1}$ is uniquely determined (Proposition 1.1)
3. $(a^{-1})^{-1} = a$ and $(ab)^{-1} = b^{-1}a^{-1}$ (Proposition 1.1)
4. The generalized associative law: any bracketing of $a_1 \star a_2 \star \cdots \star a_n$ gives the same result
5. Cancellation laws hold: $au = av \implies u = v$ and $ub = vb \implies u = v$ (Proposition 1.2)
6. Axiom (ii) ensures a group is always nonempty

# Construction / Recognition
## To Construct/Create:
1. Start with a set G and a binary operation $\star$
2. Verify closure, associativity, existence of identity, and existence of inverses

## To Identify/Recognize:
1. Check the set is nonempty
2. Verify the four axioms (closure, associativity, identity, inverses)

# Context & Application
Groups are the central object of study in Part I of the text. They arise naturally in number theory (integers under addition), geometry (symmetry groups), analysis (groups of transformations), and algebra (permutation groups, matrix groups). The abstract definition, formalized by Dyck and Weber in 1882, unifies these diverse examples.

# Examples
**Example 1** (p. 18): $\mathbb{Z}, \mathbb{Q}, \mathbb{R}, \mathbb{C}$ are groups under addition with $e = 0$ and $a^{-1} = -a$.
**Example 2** (p. 18): $\mathbb{Q} - \{0\}, \mathbb{R} - \{0\}, \mathbb{C} - \{0\}$ are groups under multiplication with $e = 1$.
**Example 3** (p. 18): $\mathbb{Z} - \{0\}$ is NOT a group under multiplication (2 has no inverse in $\mathbb{Z}$).
**Example 4** (p. 19): $\mathbb{Z}/n\mathbb{Z}$ is an abelian group under addition; $(\mathbb{Z}/n\mathbb{Z})^\times$ under multiplication.

# Relationships
## Builds Upon
- **binary-operation** — groups require an associative binary operation

## Enables
- **subgroup** — subsets that are groups under the restricted operation
- **homomorphism** — structure-preserving maps between groups
- **quotient-group** — groups formed from cosets of normal subgroups
- **group-action** — groups acting on sets

## Related
- **abelian-group** — commutative groups
- **order-of-a-group** — cardinality of the underlying set

## Contrasts With
- **monoid** — a monoid has associativity and identity but not necessarily inverses

# Common Errors
- **Error**: Assuming the group operation is commutative. **Correction**: Only abelian groups are commutative; many important groups (e.g., $S_n$ for $n \geq 3$, $D_{2n}$) are non-abelian.
- **Error**: Forgetting to check associativity. **Correction**: Associativity is an axiom that must be verified; it does not follow from the other axioms.

# Common Confusions
- **Confusion**: Thinking a set with a binary operation is automatically a group. **Clarification**: A group requires associativity, an identity, AND inverses. A set with just an associative operation and identity is a monoid, not a group.
- **Confusion**: Confusing the identity element with the number 0 or 1. **Clarification**: The identity depends on the operation: it is 0 for additive groups and 1 for multiplicative groups.

# Source Reference
Chapter 1: Introduction to Groups, Section 1.1 "Basic Axioms and Examples," pages 17-21, Propositions 1-2.

# Verification Notes
- Definition source: direct from source pp. 17-18
- Confidence rationale: central definition of the chapter, explicitly stated
- Uncertainties: none
- Cross-reference status: verified
