---
concept: Binary Operation
slug: binary-operation
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
  - "operation"
prerequisites:
  - set
  - function
extends: []
related:
  - group
  - associativity
  - commutativity
contrasts_with: []
answers_questions:
  - "What is a binary operation?"
  - "What does it mean for a binary operation to be associative?"
  - "What does it mean for elements to commute?"
---

# Quick Definition
A binary operation $\star$ on a set G is a function $\star: G \times G \to G$. It is associative if $(a \star b) \star c = a \star (b \star c)$ for all elements, and commutative if $a \star b = b \star a$ for all elements.

# Core Definition
(1) A *binary operation* $\star$ on a set G is a function $\star: G \times G \to G$. We write $a \star b$ for $\star(a, b)$. (2) The operation is *associative* if $a \star (b \star c) = (a \star b) \star c$ for all $a, b, c \in G$. (3) Elements a and b *commute* if $a \star b = b \star a$; the operation is *commutative* if all pairs commute. A subset H is *closed* under $\star$ if $a \star b \in H$ for all $a, b \in H$ (Dummit & Foote, pp. 16-17).

# Prerequisites
- **Set** — operations are defined on sets
- **Function** — a binary operation is a function from $G \times G$ to $G$

# Key Properties
1. Closure: a binary operation on G always produces elements of G
2. Associativity is not automatic and must be verified
3. A closed subset inherits associativity and commutativity automatically
4. Subtraction on $\mathbb{Z}$ is a non-associative, non-commutative binary operation

# Construction / Recognition
## To Identify/Recognize:
1. Check the operation maps $G \times G$ into $G$ (closure)
2. For associativity, verify $(a \star b) \star c = a \star (b \star c)$ for all triples

# Context & Application
Binary operations are the starting point for defining groups. A group is a set with an associative binary operation satisfying identity and inverse axioms.

# Examples
**Example 1** (p. 17): Addition is a commutative binary operation on $\mathbb{Z}$.
**Example 2** (p. 17): Subtraction is not a binary operation on $\mathbb{Z}^+$ since $a - b$ may not be positive.
**Example 3** (p. 17): The cross product on $\mathbb{R}^3$ is not associative and not commutative.

# Relationships
## Builds Upon
- **set**, **function**

## Enables
- **group** — a group is a set with an associative binary operation plus identity and inverses

## Related
- **associativity** — key property of binary operations
- **commutativity** — when elements commute

# Common Errors
- **Error**: Assuming closure without checking. **Correction**: Always verify that the operation maps the set into itself, especially for subsets.

# Common Confusions
- **Confusion**: Confusing "binary" with "having two outputs." **Clarification**: Binary means the operation takes two inputs; it always produces exactly one output.

# Source Reference
Chapter 1: Introduction to Groups, Section 1.1 "Basic Axioms and Examples," pages 16-17.

# Verification Notes
- Definition source: direct from source pp. 16-17
- Confidence rationale: explicitly defined
- Uncertainties: none
- Cross-reference status: verified
