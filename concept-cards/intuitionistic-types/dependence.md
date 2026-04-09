---
# === CORE IDENTIFICATION ===
concept: Dependence
slug: dependence

# === CLASSIFICATION ===
category: formal-system
subcategory: null
tier: intermediate

# === PROVENANCE ===
source: "An Intuitionistic Theory of Types"
source_slug: intuitionistic-types
authors: "Per Martin-Lof"
chapter: "Formalization of an Intuitionistic Theory of Types"
chapter_number: 2
pdf_page: 9
section: "2.1"

# === CONFIDENCE ===
extraction_confidence: high

# === VARIANTS ===
aliases:
  - "variable dependence"
  - "dependence on variables"

# === TYPED RELATIONSHIPS ===
prerequisites:
  - variable
  - type
extends: []
related:
  - variable-restrictions
contrasts_with: []

# === COMPETENCY QUESTIONS ===
answers_questions:
  - "What must I know before understanding dependent types?"
---

# Quick Definition

Dependence is the inductively defined relation specifying which variables a term or type depends on: it depends on all its free variables and on all variables on which the types of its free variables depend.

# Core Definition

Martin-Lof writes in Section 2.1: "The notion of dependence is defined inductively by stipulating that a term or type depends on all its free variables as well as on all variables on which the types of its free variables depend. Consequently, a term or type is closed if and only if it depends on no variables at all."

The inductive character is crucial: if b[x] has a free variable x of type A[y], then b depends on x directly (as a free variable) and also on y (because A[y] depends on y). This chain can continue transitively through the types of variables.

# Prerequisites

- variable: Dependence is a relation between terms/types and variables.
- type: The inductive step passes through the types of free variables.

# Key Properties

1. A term or type depends on all its free variables (base case).
2. A term or type depends on all variables on which the types of its free variables depend (inductive step).
3. A term or type is closed if and only if it depends on no variables at all.
4. Dependence is transitive through the typing of variables.

# Construction / Recognition

## To Determine Dependence:
1. Identify all free variables of the term or type.
2. For each free variable x of type A, recursively determine the variables on which A depends.
3. The term or type depends on the union of: (a) its free variables, and (b) the variables their types depend on.

## To Verify Closure:
1. Compute the full dependence set as above.
2. If the set is empty, the term or type is closed.

# Context & Application

Dependence is the key subtlety underlying the variable restrictions in Martin-Lof's theory. It captures the fact that in a dependently typed system, using a term of type B[x] implicitly depends not just on the free variables visible in the term but also on the variables that appear in the types of those free variables. This is essential for the soundness of binding operations.

# Examples

If x is a variable of type N (no dependencies) and b[x] has x as its only free variable, then b[x] depends only on x.

If y is a variable of type A, and x is a variable of type B[y] (which depends on y), and b[x] has x as a free variable, then b[x] depends on both x and y -- even if y does not appear free in b[x] itself.

# Relationships

## Builds Upon
- variable: Dependence is defined in terms of free variables and their types.
- type: The inductive definition passes through the types of variables.

## Enables
- variable-restrictions: The restrictions on binding are formulated in terms of dependence.

## Related
- cartesian-product-of-a-family-of-types: Dependent types make the dependence relation non-trivial.
- disjoint-union-of-a-family-of-types: Similarly involves dependent types.

# Common Errors

- **Error**: Assuming a term depends only on the variables that appear syntactically in it.
  **Correction**: A term also depends on variables that appear in the types of its free variables, even if those variables are not syntactically present in the term itself.

# Common Confusions

- **Confusion**: Confusing "contains x as a free variable" with "depends on x."
  **Clarification**: Dependence is strictly more general. A term can depend on a variable y without y appearing free in it, if y appears in the type of one of its free variables.

# Source Reference

Martin-Lof, P. (1972). "An Intuitionistic Theory of Types." Section 2.1: definition of dependence.

# Verification Notes

Confidence: high. The definition is explicitly given in Section 2.1 with a clear inductive formulation.
