---
concept: Splitting Field
slug: splitting-field
category: field-theory
subcategory: splitting-fields
tier: intermediate
source: "Abstract Algebra"
source_slug: abs-alg
authors: "David S. Dummit, Richard M. Foote"
chapter: "Field Theory"
chapter_number: 13
pdf_page: 536
section: "13.4 Splitting Fields and Algebraic Closures"
extraction_confidence: high
aliases: []
prerequisites:
  - field-extension
  - algebraic-extension
  - irreducible-polynomial
extends: []
related:
  - algebraic-closure
  - normal-extension
  - galois-extension
contrasts_with: []
answers_questions:
  - "What is a splitting field?"
  - "How do I determine the splitting field of a polynomial?"
---

# Quick Definition
The splitting field of $f(x) \in F[x]$ over F is the smallest extension K of F in which $f(x)$ factors completely into linear factors. It exists and is unique up to isomorphism.

# Core Definition
The splitting field of a polynomial $f(x) \in F[x]$ over F is a field extension K of F such that (1) $f(x)$ splits completely into linear factors in K[x], and (2) K is generated over F by the roots of $f(x)$. The splitting field exists for any polynomial and is unique up to isomorphism over F (Dummit & Foote, pp. 536-540).

# Prerequisites
- **field-extension** — A splitting field is a field extension
- **algebraic-extension** — Splitting fields are algebraic
- **irreducible-polynomial** — Roots of irreducible factors generate the extension

# Key Properties
1. Existence: always exists (adjoin roots one at a time)
2. Uniqueness: unique up to F-isomorphism
3. $[K:F] \leq n!$ where $n = \deg f$
4. A splitting field of a separable polynomial is a Galois extension
5. K/F is normal iff K is a splitting field of some polynomial over F

# Construction / Recognition
## To Construct:
1. Factor $f(x)$ into irreducibles over F
2. Adjoin a root of one irreducible factor to get $F_1 = F(\alpha_1)$
3. Factor $f(x)$ over $F_1$ and repeat
4. Continue until $f(x)$ splits completely

# Context & Application
Splitting fields are the natural extensions to study for Galois theory. They are the "just right" extensions: large enough for $f(x)$ to split, but no larger than necessary.

# Examples
**Example 1** (p. 537): The splitting field of $x^2 + 1$ over $\mathbb{R}$ is $\mathbb{C} = \mathbb{R}(i)$.
**Example 2** (p. 537): The splitting field of $x^3 - 2$ over $\mathbb{Q}$ has degree 6 over $\mathbb{Q}$ (need $\sqrt[3]{2}$ and $\omega = e^{2\pi i/3}$).

# Relationships
## Builds Upon
- **field-extension**, **algebraic-extension**

## Enables
- **galois-extension** — Splitting field of a separable polynomial
- **normal-extension** — K/F normal iff K is a splitting field

# Source Reference
Chapter 13, Section 13.4, pp. 536-543.

# Verification Notes
- Confidence: HIGH — fundamental concept with existence/uniqueness theorem
