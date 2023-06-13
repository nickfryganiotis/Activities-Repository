import { specialNeeds } from "./special_needs"
import { didacticStrategies } from "./didactic_strategies"
import { competencesDefinitions } from "./emosocio_competences"

export const filtersDefinitions = [
    {
        id: 'age_target_group',
        title: 'Age',
        caption: 'What is the target group age?',
        options: [
            {
                id: '6-8',
                value: false
            },
            {
                id: '9-12',
                value: false
            },
            {
                id: '13-18',
                value: false
            }
        ],
    },
    {
        id: 'periodicity',
        title: 'Periodicity',
        caption: 'How often is the activity repeated?',
        options: [
            {
                id: 'one-time',
                value: false
            },
            { 
                id: 'daily',
                value: false
            },
            {
                id: 'weekly',
                value: false
            },
            {
                id: 'monthly',
                value: false
            }
        ],
    },
    {
        id: 'presence',
        title: 'Presence',
        caption: 'What type of presence is required?',
        options: [
            {
                id: 'online',
                value: false
            },
            {
                id: 'in-person',
                value: false
            },
            {
                id: 'both',
                value: false
            }
        ]
    },
    {
        id: 'duration',
        title: 'Duration',
        caption: 'How long does the activity last?',
        options: [
            {
                id: '1 lective hour',
                value: false
            },
            {
                id: '2 lective hours',
                value: false
            },
            {
                id: '3 lective hours',
                value: false
            }
        ]
    },
    {
        id: 'sub_grouping',
        title: 'Subgrouping',
        caption: 'How is the group divided?',
        options: [
            {
                id: 'individual',
                value: false
            },
            {
                id: 'small group (2 - 4)',
                value: false
            },
            {
                id: 'medium group (5 - 7)',
                value: false
            },
            {
                id: 'large group (8 - 10)',
                value: false
            },
            {
                id: 'whole class',
                value: false
            }
        ]
    },
    {
        id: 'teacher_role',
        title: 'Teacher role',
        caption: 'What is the teacher role?',
        options: [
            {
                id: 'leader',
                value: false
            },
            {
                id: 'facilitator',
                value: false
            },
            {
                id: 'observer',
                value: false
            }
        ]
    },
    {
        id: 'competences',
        title: 'Competences',
        caption: 'What competences are developed?',
        options: Object.keys(competencesDefinitions).map((competence) => {
            return {
                id: competence,
                value: false
            }
        })
    },
    {
        id: 'didactic_strategies',
        title: 'Didactic strategy',
        caption: 'What didactic strategies are used?',
        options: Object.keys(didacticStrategies).map((strategy) => {
            return {
                id: strategy,
                value: false
            }
        })
    },
    {
        id: 'special_needs',
        title: 'Special needs',
        caption: 'What special needs are addressed?',
        options: Object.keys(specialNeeds).map((need) => {
            return {
                id: need,
                value: false
            }
        })
    }
]