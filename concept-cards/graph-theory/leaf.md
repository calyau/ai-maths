---
concept: Leaf
slug: leaf

category: trees-and-forests
tier: foundational

source: "Graph Theory"
source_slug: graph-theory
authors: "Reinhard Diestel"
chapter: "The Basics"
chapter_number: 1
pdf_page: 23
section: "1.5 Trees and forests"

extraction_confidence: high

aliases: []

prerequisites:
  - tree
  - degree
extends: []
related:
  - rooted-tree
contrasts_with: []

answers_questions:
  - "What is a leaf of a tree?"
---

# Quick Definition
A leaf is a vertex of degree 1 in a tree, except that the root of a rooted tree is never called a leaf even if it has degree 1.

# Core Definition
The vertices of degree 1 in a tree are its leaves. Every non-trivial tree has a leaf. Note: the root of a tree is never called a leaf, even if it has degree 1 (Diestel, p. 13, footnote 5).

# Prerequisites
- **Tree** — leaves are vertices of trees
- **Degree** — a leaf has degree 1

# Key Properties
1. A leaf has exactly one neighbor
2. Every non-trivial tree has at least one leaf
3. Removing a leaf from a tree yields another tree
4. A tree has at least Delta(T) leaves (Exercise 16)

# Context & Application
Leaves are crucial for inductive proofs about trees: removing a leaf preserves the tree property.

# Relationships
## Builds Upon
- **tree**, **degree**

# Source Reference
Chapter 1: The Basics, Section 1.5, page 13 (pdf p. 23).

# Verification Notes
- Direct from p. 13
- Confidence: HIGH
