export const parameters = {
    'age': [
        {
            label: '6 - 8',
            value: {
                min: 6,
                max: 8
            }
        },
        {
            label: '9 - 12',
            value: {
                min: 9,
                max: 12
            }
        },
        {
            label: '13 - 18',
            value: {
                min: 13,
                max: 18
            }
        }
    ],
    'periodicity': [
        'weekly',
        'monthly',
        'quarterly',
        'one time'
    ],
    'duration': [
        '1 hour',
        '2 hours',
        '3 hours',
        '4 hours',
    ],
    'presence': [
        'online',
        'in person',
        'both'
    ],
    'subgrouping' : [
        'individual',
        'small group',
        'large group',
        'whole class'
    ],
    'teacherRole' : [
        'facilitator',
        'leader',
        'observer'
    ]

}