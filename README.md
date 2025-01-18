# **Binary Search and Linear Search Implementation**

## **Overview**

This project implements two core search algorithms: **Binary Search** and **Linear Search**. The purpose is to demonstrate the basic principles of searching algorithms, their use cases, and efficiency.

---

## **Purpose of the Code**

- **Linear Search**: A straightforward algorithm that searches each element of a list sequentially until it finds the target element.

- **Binary Search**: A more efficient algorithm that works on **sorted lists**. It divides the list into two halves and continues searching in the relevant half based on whether the target is smaller or larger than the middle element.

---

## **Time Complexity**

### **Linear Search:**

- **Best Case**: `O(1)` — This happens if the target element is at the **first position**.
- **Worst Case**: `O(n)` — Occurs when the target element is at the **last position** or **not in the list** at all.

---

### **Binary Search:**

- **Best Case**: `O(1)` — This occurs when the target element is found in the **middle of the list**.

- **Worst Case**: `O(log n)` — This is the ideal time complexity for binary search when applied to a **sorted list**. However, if binary search is used on an **unsorted list**, the worst-case time complexity can degrade to `O(n)`, as the list may need to be scanned entirely.

  In practice, **O(n)** for binary search is when the list is **not sorted**, and the algorithm must traverse the entire list to find the element.

---

## **How to Run the Program**

1. **Clone the repository** to your local machine.
2. **Navigate to the project directory**.
3. **Run the program**.
4. The program will prompt you to input a **list of numbers** and a **target value**.
5. It will then perform both **Linear Search** and **Binary Search** (if the list is sorted) and display the **index** of the target element if found. If not found, it will indicate that the target does **not exist** in the list.

---



