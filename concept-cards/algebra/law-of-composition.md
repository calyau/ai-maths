---
concept: Law of Composition
slug: law-of-composition
category: group-theory
subcategory: null
tier: foundational
source: "Algebra"
source_slug: algebra
authors: "Michael Artin"
chapter: "Groups"
chapter_number: 2
pdf_page: 48
section: "2.1 Laws of Composition"
extraction_confidence: high
aliases:
  - "binary operation"
  - "operation"
prerequisites: []
extends: []
related:
  - group
  - associative-law
  - commutative-law
contrasts_with: []
answers_questions:
  - "What is a group?"
---

# Quick Definition

A law of composition on a set S is a rule for combining any pair of elements a, b of S to produce another element of S. Formally, it is a map S x S -> S.

# Core Definition

A law of composition on a set S is any rule for combining pairs a, b of elements of S to get another element p of S. Formally, it is a function S x S -> S. The result may be written ab, a x b, a + b, etc. A law is associative if (ab)c = a(bc), and commutative if ab = ba (Artin, pp. 48-49).

# Prerequisites

This is a foundational concept with no prerequisites within this source.

# Key Properties

1. A law of composition is a function of two variables from S x S to S
2. Closure is built into the definition (the result is in S)
3. May or may not be associative, commutative, or have an identity

# Construction / Recognition

## To Construct:
1. Define a set S
2. Define a rule that assigns to each pair (a,b) in S x S an element of S

## To Recognize:
1. A way to combine two elements of a set to get another element of the same set

# Context & Application

Laws of composition are the starting point for abstract algebra. Artin begins with this most general concept before specializing to groups. Examples include addition and multiplication of numbers, matrix multiplication, and composition of functions.

# Examples

**Example 1** (p. 49): Composition of functions from a set T to itself is a law of composition that is associative but not commutative.

**Example 2** (p. 49): The multiplication table for maps from {a,b} to itself shows four maps with a non-commutative law.

# Relationships

## Enables
- **Group** — A set with an associative law of composition, identity, and inverses
- **Associative law** — A property a law may or may not have
- **Commutative law** — A property a law may or may not have

# Common Errors

- **Error**: Assuming all laws of composition are commutative
  **Correction**: Matrix multiplication and function composition are not commutative

# Common Confusions

- **Confusion**: Confusing a law of composition with a function
  **Clarification**: A law of composition IS a function, specifically one from S x S to S

# Source Reference

Chapter 2: Groups, Section 2.1, pages 48-49.

# Verification Notes

- Definition source: Direct from Section 2.1, p. 48
- Confidence rationale: Explicitly defined
- Uncertainties: None
- Cross-reference status: Verified
