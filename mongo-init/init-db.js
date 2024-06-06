db.getSiblingDB('admin').auth('admin', 'admin');
db = db.getSiblingDB("project-tracker-db");
db.createCollection("projects");

db.projects.insertMany([
    {
        "name": "Kitchen Remodel",
        "description": "Complete renovation of the kitchen, including new cabinets, countertops, and updated appliances.",
        "startDate": "2024-07-01",
        "endDate": "2024-09-15",
        "budget": 15000,
        "status": "Planned",
        "contractorDetails": {
            "name": "GoodBuild Renovations",
            "contact": "+1234567890"
        },
        "tasks": [
            {
                "taskName": "Demolition",
                "startDate": "2024-07-01",
                "endDate": "2024-07-05",
                "status": "Pending"
            },
            {
                "taskName": "Cabinet Installation",
                "startDate": "2024-07-10",
                "endDate": "2024-08-10",
                "status": "Pending"
            },
            {
                "taskName": "Appliance Setup",
                "startDate": "2024-08-15",
                "endDate": "2024-09-05",
                "status": "Pending"
            },
            {
                "taskName": "Final Touches",
                "startDate": "2024-09-10",
                "endDate": "2024-09-15",
                "status": "Pending"
            }
        ]
    },
    {
        "name": "Bathroom Refresh",
        "description": "Updating the master bathroom with new fixtures, tiles, and a modern shower system.",
        "startDate": "2024-10-01",
        "endDate": "2024-11-20",
        "budget": 10000,
        "status": "Planned",
        "contractorDetails": {
            "name": "ModernHome Solutions",
            "contact": "+0987654321"
        },
        "tasks": [
            {
                "taskName": "Tile Replacement",
                "startDate": "2024-10-01",
                "endDate": "2024-10-15",
                "status": "Pending"
            },
            {
                "taskName": "Fixture Installation",
                "startDate": "2024-10-20",
                "endDate": "2024-11-05",
                "status": "Pending"
            },
            {
                "taskName": "Shower System Setup",
                "startDate": "2024-11-10",
                "endDate": "2024-11-15",
                "status": "Pending"
            },
            {
                "taskName": "Cleanup and Finalization",
                "startDate": "2024-11-16",
                "endDate": "2024-11-20",
                "status": "Pending"
            }
        ]
    }
]);

print("Projects collection and sample projects created successfully");