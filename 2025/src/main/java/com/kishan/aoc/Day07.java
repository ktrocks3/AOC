package com.kishan.aoc;

import java.io.IOException;
import java.net.URISyntaxException;
import java.nio.file.Files;
import java.nio.file.Path;
import java.util.ArrayList;
import java.util.Arrays;
import java.util.List;

public class Day07 {
    public static void main(String[] args) throws URISyntaxException, IOException {
        List<String> example = Files.readAllLines(Path.of(ClassLoader.getSystemResource("Day07/example.txt").toURI()));
        List<String> input = Files.readAllLines(Path.of(ClassLoader.getSystemResource("Day07/input.txt").toURI()));

        assert Part1(example) == 21;
        System.out.println(Part1(input));

        assert Part2(example) == 40;
        System.out.println(Part2(input));
    }

    private static int Part1(List<String> input) {
        int counter = 0;
        int[][] grid = encode(input);
        for (int i = 0; i < grid.length - 1; i++) {
            int[] row = grid[i];
            for (int j = 0; j < row.length; j++) {
                int cell = row[j];
                int below = grid[i + 1][j];
                if (cell == 1 && below == 0) {
                    grid[i + 1][j] = 1;
                } else if (cell == 1 && below == 2) {
                    counter += 1;

                    if (j > 0) {
                        int belowL = grid[i + 1][j - 1];
                        if (belowL == 0) {
                            grid[i + 1][j - 1] = 1;
                        }
                    }
                    if (j < row.length - 1) {
                        int belowR = grid[i + 1][j + 1];
                        if (belowR == 0) {
                            grid[i + 1][j + 1] = 1;
                        }
                    }

                }
            }
        }
        return counter;
    }

    private static long Part2(List<String> input) {
        int[][] grid = encode(input);
        long[] timelines = new long[grid[0].length];
        int index = 0;
        for (int i = 0; i < grid[0].length; i++) {
            if (grid[0][i] == 1) {
                index = i;
            }
        }
        timelines[index] = 1;
        for (int i = 1; i < grid.length - 1; i++) {
            for (int j = 0; j < timelines.length; j++) {
                if (timelines[j] >= 1) {
                    if (grid[i + 1][j] == 2) {
                        if (j != timelines.length - 1) timelines[j + 1] += timelines[j];
                        if (j != 0) timelines[j - 1] += timelines[j];
                        timelines[j] = 0;
                    }
                }
            }
        }

        return Arrays.stream(timelines).sum();
    }

    private static void printGrid(int[][] grid) {
        for (int[] line : grid) {
            StringBuilder s = new StringBuilder();
            for (int i : line) {
                switch (i) {
                    case 0:
                        s.append('.');
                        break;
                    case 1:
                        s.append('|');
                        break;
                    case 2:
                        s.append('^');
                        break;
                }
            }
            System.out.println(s);
        }
    }

    private static int[][] encode(List<String> input) {
        int[][] grid = new int[input.size()][input.getFirst().length()];
        for (int i = 0; i < input.size(); i++) {
            String line = input.get(i);
            for (int j = 0; j < line.length(); j++) {
                switch (line.charAt(j)) {
                    case 'S':
                        grid[i][j] = 1;
                        break;
                    case '^':
                        grid[i][j] = 2;
                        break;
                    default:
                        grid[i][j] = 0;
                        break;

                }
            }
        }
        return grid;
    }


}
