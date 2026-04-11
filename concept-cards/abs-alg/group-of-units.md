---
concept: Group of Units
slug: group-of-units
category: ring-theory
subcategory: basic-definitions
tier: foundational
source: "Abstract Algebra"
source_slug: abs-alg
authors: "David S. Dummit, Richard M. Foote"
chapter: "Introduction to Rings"
chapter_number: 7
pdf_page: 227
section: "7.1 Basic Definitions and Examples"
extraction_confidence: high
aliases:
  - "unit group"
prerequisites:
  - ring-with-identity
  - unit
extends: []
related:
  - field
  - chinese-remainder-theorem
contrasts_with: []
answers_questions:
  - "What is the group of units of a ring?"
---

# Quick Definition
The group of units $R^{\times}$ of a ring R with identity is the set of all units in R, which forms a group under multiplication.

# Core Definition
The units in a ring R form a group under multiplication, denoted $R^{\times}$ and called the *group of units* of R. A field is a commutative ring where $F^{\times} = F - \{0\}$ (Dummit & Foote, p. 227).

# Prerequisites
- **Ring with identity** — Units require a multiplicative identity
- **Unit** — The elements of the group

# Key Properties
1. $R^{\times}$ is a group under multiplication
2. $\mathbb{Z}^{\times} = \{\pm 1\}$
3. $(\mathbb{Z}/n\mathbb{Z})^{\times} = \{\bar{a} \mid \gcd(a, n) = 1\}$, with order $\varphi(n)$
4. CRT gives $(\mathbb{Z}/mn\mathbb{Z})^{\times} \cong (\mathbb{Z}/m\mathbb{Z})^{\times} \times (\mathbb{Z}/n\mathbb{Z})^{\times}$ when $\gcd(m,n) = 1$

# Examples
**Example 1** (p. 228): $\mathbb{Z}^{\times} = \{\pm 1\}$.

**Example 2** (p. 228): $\mathbb{Z}[i]^{\times} = \{\pm 1, \pm i\}$.

**Example 3** (p. 228): In $\mathbb{Z}/n\mathbb{Z}$, the units are elements coprime to n.

# Source Reference
Chapter 7, Section 7.1, page 227.

# Verification Notes
- Definition: Direct from p. 227
- Confidence: HIGH — explicit definition
