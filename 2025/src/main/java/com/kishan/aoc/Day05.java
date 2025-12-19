package com.kishan.aoc;

import java.io.IOException;
import java.net.URISyntaxException;
import java.nio.file.Files;
import java.nio.file.Path;
import java.util.ArrayList;
import java.util.Comparator;
import java.util.HashSet;
import java.util.List;

public class Day05 {
    record Range(long start, long end) {
    }

    public static void main(String[] args) throws URISyntaxException, IOException {
        List<String> example = Files.readAllLines(Path.of(ClassLoader.getSystemResource("Day5/example.txt").toURI()));
        List<String> input = Files.readAllLines(Path.of(ClassLoader.getSystemResource("Day5/input.txt").toURI()));

        assert Part1(example) == 3;
        System.out.println("Part 1: " + Part1(input));

        assert Part2(example) == 14;
        System.out.println("Part 2: " + Part2(input));

    }

    private static int Part1(List<String> input) {
        int fresh = 0;
        List<Range> ranges = new ArrayList<>();
        boolean firstPart = true;
        for (String line : input) {
            if (line.isEmpty()) {
                firstPart = false;
                continue;
            }
            if (firstPart) {
                long start = Long.parseLong(line.split("-")[0]);
                long end = Long.parseLong(line.split("-")[1]);
                ranges.add(new Range(start, end));
            } else {
                long value = Long.parseLong(line);
                for (Range r : ranges) {
                    if (value >= r.start() && value <= r.end()) {
                        fresh++;
                        break;
                    }
                }
            }
        }
        ranges.sort(Comparator.comparing(Range::start));
        return fresh;
    }

    private static long Part2(List<String> input) {
        long total = 0;
        List<Range> ranges = new ArrayList<>();
        for (String line : input) {
            if (line.isEmpty()) {
                break;
            }
            long start = Long.parseLong(line.split("-")[0]);
            long end = Long.parseLong(line.split("-")[1]);
            ranges.add(new Range(start, end));
        }
        ranges.sort(Comparator.comparingLong(Range::start));
        List<Range> merged = new ArrayList<>();
        Range current = ranges.getFirst();
        for (int i = 1; i < ranges.size(); i++) {
            Range next = ranges.get(i);
            if (next.start() <= current.end() + 1) {
                current = new Range(current.start(), Math.max(current.end(), next.end()));
            } else {
                merged.add(current);
                current = next;
            }
        }
        merged.add(current);
        for (Range range : merged) {
            total += (range.end - range.start + 1);
        }


        return total;
    }


}
