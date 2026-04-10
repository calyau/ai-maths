---
concept: Dynkin Diagram
slug: dynkin-diagram
category: root-systems
subcategory: null
tier: intermediate
source: "Algebraic Groups, Lie Groups, and their Arithmetic Subgroups"
source_slug: groups-subgroups
authors: "J.S. Milne"
chapter: "The Structure of Semisimple Lie Algebras and Algebraic Groups in Characteristic Zero"
chapter_number: 3
pdf_page: 302
section: "Classification of root systems by Dynkin diagrams"
extraction_confidence: high
aliases:
  - "Dynkin graph"
prerequisites:
  - root-system
  - cartan-matrix
  - coxeter-graph
extends:
  - coxeter-graph
related:
  - classification-of-semisimple-lie-algebras
contrasts_with:
  - coxeter-graph
answers_questions:
  - "What is a Dynkin diagram?"
  - "How do Dynkin diagrams classify root systems?"
  - "How do I classify a root system using its Dynkin diagram?"
---

# Quick Definition

A Dynkin diagram is a decorated graph that classifies indecomposable root systems. Its nodes correspond to simple roots, edges encode the angles between them, and arrows point from longer to shorter roots.

# Core Definition

Let (V, R) be a root system and S a base. The **Coxeter graph** has nodes indexed by elements of S, with two distinct nodes joined by n(α,β)·n(β,α) edges. The **Dynkin diagram** is obtained from the Coxeter graph by adding arrowheads on the multiple edges, pointing toward the shorter root. The Dynkin diagram determines the Cartan matrix and hence the root system (Milne, §1h, p. 302).

# Prerequisites

- **Root system** — Dynkin diagrams classify root systems
- **Cartan matrix** — The Dynkin diagram encodes the same information
- **Coxeter graph** — The Dynkin diagram refines the Coxeter graph

# Key Properties

1. The Coxeter graph is connected if and only if the root system is indecomposable (Proposition 1.16)
2. The Dynkin diagram determines the Cartan matrix (Coxeter graph alone does not, e.g., B_n vs C_n)
3. The arrowhead distinguishes which root is longer when there are multiple edges

# Construction / Recognition

## To Construct:
1. Choose a base S for the root system
2. Draw one node for each simple root α ∈ S
3. Connect nodes α, β with n(α,β)·n(β,α) edges (0, 1, 2, or 3)
4. For double/triple edges, add an arrow pointing toward the shorter root

## To Read Off:
- Single edge: angle π/3, roots of equal length
- Double edge with arrow: angle π/4, length ratio √2
- Triple edge with arrow: angle π/6, length ratio √3
- No edge: orthogonal roots

# Context & Application

The classification of indecomposable Dynkin diagrams (Theorem 1.17) is one of the most celebrated results in mathematics. It gives a complete list: A_n (n≥1), B_n (n≥2), C_n (n≥3), D_n (n≥4), E_6, E_7, E_8, F_4, G_2. This classifies all simple Lie algebras (over algebraically closed fields of characteristic zero) and all simple algebraic groups.

# Examples

**Example 1** (p. 302): The Dynkin diagrams of rank 2 root systems: A₁×A₁ (two disconnected nodes), A₂ (two nodes, single edge), B₂ (two nodes, double edge with arrow), G₂ (two nodes, triple edge with arrow).

**Example 2** (p. 302): The root system in Example 1.4/1.13 has Dynkin diagram A_n (a chain of n nodes connected by single edges).

# Relationships

## Builds Upon
- **Coxeter graph** — Dynkin diagram adds arrow information
- **Cartan matrix** — Dynkin diagram encodes the same data

## Enables
- **Classification of semisimple Lie algebras** — Via root system classification
- **Classification of semisimple algebraic groups** — Via root system and lattice data

## Contrasts With
- **Coxeter graph** — Does not distinguish B_n from C_n

# Common Confusions

- **Confusion**: Believing Coxeter graph and Dynkin diagram carry the same information
  **Clarification**: The Coxeter graph only records n(α,β)·n(β,α), not the individual values; the arrow in the Dynkin diagram resolves this ambiguity

# Source Reference

Chapter III, Section 1h, pages 301–304. See list of diagrams on p. 304 (Section 1j).

# Verification Notes

- Definition source: Direct from §1h, p. 302
- Confidence: HIGH — explicit definition and classification theorem
- Uncertainties: None
