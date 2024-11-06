from typing import List


class Solution:
    def asteroidCollision(self, asteroids: List[int]) -> List[int]:
        stack = []

        for rock in asteroids:
            while stack and rock < 0 and stack[-1] > 0:
                if stack[-1] < -rock:
                    stack.pop()
                elif stack[-1] == -rock:
                    stack.pop()
                    break
                else:

                    break
            else:
                stack.append(rock)

        return stack


def test_solution(asteroids, expected):
    solution = Solution()
    result = solution.asteroidCollision(asteroids)
    print(f"Input: asteroids = {asteroids}")
    print(f"Expected: {expected}, Got: {result}")
    print(f"Test {'PASSED' if result == expected else 'FAILED'}")
    print("-" * 50)


if __name__ == "__main__":
    # Test Case 1: Basic collision, one survives
    test_solution([5, 10], [5, 10])

    # Test Case 2: Equal collision, both destroyed
    test_solution([8, -8], [])

    # Test Case 3: One asteroid moving left, no collision
    test_solution([10, 2, -5], [10])

    # # Test Case 4: No collision, all move in the same direction
    # test_solution([-2, -1, 1, 2], [-2, -1, 1, 2])

    # Test Case 5: Complex sequence with multiple collisions
    test_solution([1, -2, -2, -2, 5, 10, -10, 1, -1], [-2, -2, -2, 5, 1])

    # Test Case 6: Large positive followed by smaller negative
    test_solution([3, -4], [-4])

    # Test Case 7: Single asteroid, no collision
    test_solution([1], [1])
    test_solution([-1], [-1])

    # Test Case 8: Two large asteroids with smaller ones between
    test_solution([10, 2, -5, -3, -8], [10])

    # Test Case 9: All asteroids moving left
    test_solution([-5, -10, -15], [-5, -10, -15])

    # Test Case 10: All asteroids moving right
    test_solution([3, 6, 9, 12], [3, 6, 9, 12])
