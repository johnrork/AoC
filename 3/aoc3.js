fs = require('fs')
toboggan = (lines, over, down) => {
    offset = 0
    count = 0
    last_line = 0

    for (i = 0; i < lines.length; i++) {
        if (last_line + down !== i)
            continue

        offset += over
        if (offset >= lines[i].length)
            offset -= lines[i].length

        if (lines[i][offset] === "#")
            count += 1
        last_line = i
    };
    return count
}

fs.readFile('trees.txt', 'utf8', (e, data) => {
    lines = data.split('\n')
    t1 = toboggan(lines, 1, 1)
    t2 = toboggan(lines, 3, 1)
    t3 = toboggan(lines, 5, 1)
    t4 = toboggan(lines, 7, 1)
    t5 = toboggan(lines, 1, 2)

    console.log('Part 1:', t2)
    console.log('Part 2:', t1 * t2 * t3 * t4 * t5)
})
