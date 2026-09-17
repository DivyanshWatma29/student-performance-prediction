const fs = require('fs');

let csv = 'attendance,study_hours,internal_marks,assignments,final_marks\n';
for (let i = 0; i < 500; i++) {
    const attendance = Math.floor(Math.random() * 51) + 50; // 50-100
    const study_hours = Math.floor(Math.random() * 14) + 1; // 1-14
    const internal_marks = Math.floor(Math.random() * 71) + 30; // 30-100
    const assignments = Math.floor(Math.random() * 11); // 0-10
    
    // Linear combination + noise
    let final_marks = 0.4 * attendance + 1.2 * study_hours + 0.3 * internal_marks + 1.5 * assignments;
    final_marks += (Math.random() * 10 - 5); // noise -5 to +5
    
    // Scale and clip
    final_marks = Math.max(0, Math.min(100, final_marks));
    
    csv += `,,,,\n`;
}
fs.writeFileSync('student_data.csv', csv);
console.log('Dataset created');
