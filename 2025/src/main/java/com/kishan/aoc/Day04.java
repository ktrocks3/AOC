package com.kishan.aoc;

import java.io.IOException;
import java.net.URISyntaxException;
import java.nio.file.Files;
import java.nio.file.Path;
import java.util.ArrayList;
import java.util.List;

public class Day04 {
    public static void main(String[] args) throws URISyntaxException, IOException {
        List<String> example = Files.readAllLines(Path.of(ClassLoader.getSystemResource("Day04/example.txt").toURI()));
        List<String> input = Files.readAllLines(Path.of(ClassLoader.getSystemResource("Day04/input.txt").toURI()));

        assert Part1(example) == 13;
        System.out.println("Part 1: " + Part1(input));

        assert Part2(example) == 43;
        System.out.println("Part 2: " + Part2(input));
    }

    private static List<Integer> surrounding(int i, int j, int row, int col) {
        List<Integer> squares = new ArrayList<>();
        for (int k = -1; k < 2; k++) {
            for (int l = -1; l < 2; l++) {
                if (k == 0 && l == 0) continue;
                int ni = i + k;
                int nj = j + l;

                if (ni >= 0 && ni < row && nj >= 0 && nj < col) {
                    squares.add(ni * col + nj);
                }
            }
        }
        return squares;
    }


    private static int Part1(List<String> input) {
        int rolls = 0;
        int row = input.size();
        int col = input.getFirst().length();
        int[][] squares = new int[row][col];
        for (int i = 0; i < input.size(); i++) {
            String s = input.get(i);
            for (int j = 0; j < s.length(); j++) {
                if (s.charAt(j) == '.') {
                    squares[i][j] += 8;
                    continue;
                }
                for (Integer cell : surrounding(i, j, row, col)) {
                    int ni = cell / col;
                    int nj = cell % col;
                    squares[ni][nj] += 1;
                }
            }
        }
        for (int[] square : squares) {
            for (int i : square) {
                if (i < 4) {
                    rolls += 1;
                }
            }
        }
        return rolls;
    }

    private static int Part2(List<String> input) {
        int rolls = 0;
        int row = input.size();
        int col = input.getFirst().length();
        int[][] squares = new int[row][col];
        for (int i = 0; i < input.size(); i++) {
            String s = input.get(i);
            for (int j = 0; j < s.length(); j++) {
                if (s.charAt(j) == '.') {
                    squares[i][j] += 8;
                    continue;
                }
                for (Integer cell : surrounding(i, j, row, col)) {
                    int ni = cell / col;
                    int nj = cell % col;
                    squares[ni][nj] += 1;
                }
            }
        }

        boolean changed;
        do {
            changed = false;
            int[][] squarescopy = new int[row][col];
            for (int i = 0; i < row; i++) {
                squarescopy[i] = squares[i].clone();
            }

            for (int i = 0; i < squares.length; i++) {
                for (int j = 0; j < squares[i].length; j++) {
                    if (squarescopy[i][j] < 4) {
                        rolls += 1;
                        squares[i][j] = 100;
                        changed = true;
                        for (Integer cell : surrounding(i, j, row, col)) {
                            int ni = cell / col;
                            int nj = cell % col;
                            squares[ni][nj] -= 1;
                        }
                    }
                }
            }
        } while (changed);

        return rolls;
    }
}
