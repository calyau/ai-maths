---
concept: Equivalence Class
slug: equivalence-class
category: group-theory
subcategory: null
tier: foundational
source: "Algebra"
source_slug: algebra
authors: "Michael Artin"
chapter: "Groups"
chapter_number: 2
pdf_page: 48
section: "2.7 Equivalence Relations and Partitions"
extraction_confidence: high
aliases:
  - "congruence class"
prerequisites:
  - equivalence-relation
extends: []
related:
  - partition
  - coset
  - integers-mod-n
contrasts_with: []
answers_questions:
  - "What is a group?"
---

# Quick Definition

The equivalence class of an element a under an equivalence relation ~ is the set C_a = {b in S : a ~ b} of all elements equivalent to a. Equivalence classes partition S into disjoint subsets.

# Core Definition

Given an equivalence relation ~ on S, the equivalence class of a is C_a = {b in S : a ~ b} (Artin, p. 69, formula 2.7.5). Equivalence classes are the subsets in the partition determined by ~ (Lemma 2.7.6). If a ~ b, then C_a = C_b.

# Prerequisites

- **Equivalence relation** — Classes are defined by an equivalence relation

# Key Properties

1. Every element belongs to exactly one class
2. C_a = C_b iff a ~ b
3. Classes are disjoint and cover S
4. A representative element can be chosen from each class

# Construction / Recognition

## To Construct:
1. Fix an element a
2. Collect all elements b with a ~ b

## To Recognize:
1. A maximal set of mutually equivalent elements

# Context & Application

Equivalence classes are the elements of quotient constructions. Congruence classes modulo n are the elements of Z/nZ. Cosets are equivalence classes for the congruence relation defined by a subgroup.

# Examples

**Example 1** (p. 69): The equivalence class of 0 modulo n is {0, +/-n, +/-2n, ...} = nZ.

**Example 2** (p. 69): In S_3, elements of the same order form equivalence classes: {1}, {x, x^2}, {y, xy, x^2y}.

# Relationships

## Builds Upon
- **Equivalence relation** — Defines the classes

## Enables
- **Partition** — Classes form a partition
- **Integers mod n** — Congruence classes
- **Quotient group** — Elements are equivalence classes (cosets)

# Common Errors

- **Error**: Thinking two elements in different classes can be equivalent
  **Correction**: If a ~ b, they are in the SAME class

# Common Confusions

- **Confusion**: Confusing the class with a representative
  **Clarification**: The class is a SET of elements; a representative is one chosen element from the set

# Source Reference

Chapter 2: Groups, Section 2.7, page 69.

# Verification Notes

- Definition source: Direct from (2.7.5), p. 69
- Confidence rationale: Explicitly defined
- Uncertainties: None
- Cross-reference status: Verified
