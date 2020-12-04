<?php
function toboggan($lines, $over, $down){
    $offset = 0;
    $count = 0;
    $last_line = 0;
    $ln_length = strlen(trim($lines[0]));

    foreach ($lines as $i => $l) {
        if ($last_line + $down != $i){
            continue;
        }
        $offset += $over;
        if ($offset >= $ln_length){
            $offset -= $ln_length;
        }
        if ($l[$offset] == '#'){
            $count += 1;
        }
        $last_line = $i;
    }
    return $count;
}

$handle = fopen('trees.txt', 'r');
$lines = array();
while (($line = fgets($handle)) !== false) {
    array_push($lines, $line);
}
fclose($handle);

$t1 = toboggan($lines, 1, 1);
$t2 = toboggan($lines, 3, 1);
$t3 = toboggan($lines, 5, 1);
$t4 = toboggan($lines, 7, 1);
$t5 = toboggan($lines, 1, 2);
echo("Part 1: ". $t2."\n");
echo("Part 2: ". $t1 * $t2 * $t3 * $t4 * $t5 . "\n");
?>
