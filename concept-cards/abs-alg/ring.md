---
concept: Ring
slug: ring
category: ring-theory
subcategory: basic-definitions
tier: foundational
source: "Abstract Algebra"
source_slug: abs-alg
authors: "David S. Dummit, Richard M. Foote"
chapter: "Introduction to Rings"
chapter_number: 7
pdf_page: 223
section: "7.1 Basic Definitions and Examples"
extraction_confidence: high
aliases:
  - "ring (algebra)"
prerequisites: []
extends: []
related:
  - commutative-ring
  - ring-with-identity
  - field
  - subring
  - ideal
contrasts_with:
  - group
  - field
answers_questions:
  - "What is a ring?"
  - "How does a ring differ from a group?"
  - "What are the axioms for a ring?"
---

# Quick Definition
A ring R is a set with two binary operations, addition (+) and multiplication (x), where (R, +) is an abelian group, multiplication is associative, and the distributive laws hold.

# Core Definition
A ring R is a set together with two binary operations + and x (called addition and multiplication) satisfying the following axioms: (i) (R, +) is an abelian group, (ii) multiplication is associative: $(a \times b) \times c = a \times (b \times c)$ for all $a, b, c \in R$, and (iii) the distributive laws hold: $(a+b) \times c = (a \times c) + (b \times c)$ and $a \times (b+c) = (a \times b) + (a \times c)$ for all $a, b, c \in R$ (Dummit & Foote, p. 223).

# Prerequisites
This is a foundational concept with no prerequisites within this source.

# Key Properties
1. (R, +) forms an abelian group with identity 0
2. Multiplication is associative
3. Both left and right distributive laws hold
4. $0a = a0 = 0$ for all $a \in R$ (Proposition 1)
5. $(-a)b = a(-b) = -(ab)$ for all $a, b \in R$
6. $(-a)(-b) = ab$ for all $a, b \in R$
7. If R has identity 1, then the identity is unique and $-a = (-1)a$

# Construction / Recognition
## To Identify a Ring:
1. Verify (R, +) is an abelian group
2. Verify multiplication is associative
3. Verify both distributive laws hold

## To Construct a Ring:
1. Start with an abelian group (R, +)
2. Define a multiplication that is associative
3. Verify both distributive laws connect addition and multiplication

# Context & Application
Rings generalize the algebraic structure of the integers $\mathbb{Z}$. The theory of rings is concerned with objects possessing two binary operations related by the distributive laws. Rings form the foundation for the study of fields, modules, and algebraic geometry. The basic theory of rings is the cornerstone for Parts II-VI of the book (Dummit & Foote, p. 223).

**Typical examples:**
- $\mathbb{Z}$, $\mathbb{Q}$, $\mathbb{R}$, $\mathbb{C}$ (commutative rings with identity)
- $\mathbb{Z}/n\mathbb{Z}$ (modular arithmetic)
- The zero ring $\{0\}$ (trivial ring)

# Examples
**Example 1** (p. 224): The integers $\mathbb{Z}$ under usual addition and multiplication form a commutative ring with identity.

**Example 2** (p. 224): $\mathbb{Q}$, $\mathbb{R}$, $\mathbb{C}$ are commutative rings with identity (in fact, fields).

**Example 3** (p. 224): The quotient group $\mathbb{Z}/n\mathbb{Z}$ is a commutative ring with identity $\overline{1}$ under modular arithmetic.

**Example 4** (p. 224): The ring $2\mathbb{Z}$ of even integers is a commutative ring without identity.

# Relationships

## Enables
- **commutative-ring** — A ring where multiplication is commutative
- **ring-with-identity** — A ring with a multiplicative identity
- **subring** — A subset that is itself a ring under the same operations
- **ideal** — A special type of subring used to form quotient rings
- **ring-homomorphism** — Structure-preserving maps between rings

## Related
- **abelian-group** — (R, +) must be an abelian group
- **polynomial-ring** — An important construction of new rings

## Contrasts With
- **group** — Has only one binary operation
- **field** — Every nonzero element has a multiplicative inverse

# Common Errors
- **Error**: Assuming every ring has a multiplicative identity
  **Correction**: The ring $2\mathbb{Z}$ of even integers has no multiplicative identity; a ring need not have a 1

- **Error**: Assuming multiplication in a ring is commutative
  **Correction**: Matrix rings $M_n(R)$ for $n \geq 2$ are noncommutative

# Common Confusions
- **Confusion**: Thinking the requirement that (R, +) be abelian is an additional axiom beyond the ring axioms
  **Clarification**: If R has a 1, commutativity of addition follows from the distributive laws; it is included in the definition for rings without identity

- **Confusion**: Confusing "ring" with "field"
  **Clarification**: A ring need not have multiplicative inverses for nonzero elements; a field is a special type of ring

# Source Reference
Chapter 7: Introduction to Rings, Section 7.1 "Basic Definitions and Examples," pages 223-228. See Definition at the beginning of the section and Proposition 1 for basic ring properties.

# Verification Notes
- Definition: Direct from p. 223, Definition (1)
- Key Properties: Proposition 1, p. 226
- Examples: All from pp. 224-225
- Confidence: HIGH — explicit, precise definition with extensive examples in source
