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
        'daily',
        'one time',
        'weekly',
        'monthly',
    ],
    'duration': [
        '1 lective hour',
        '2 lective hours',
        '3 lective hours',
    ],
    'presence': [
        'online',
        'in person',
        'both'
    ],
    'subgrouping' : [
        'individual',
        'small group (2-4)',
        'medium group (5-7)',
        'large group (8-10)',
        'whole class'
    ],
    'teacherRole' : [
        'facilitator',
        'leader',
        'observer'
    ]

}