#!/bin/bash

echo "Iniciando deploy..."
tar -czf backup_$(date +%F).tar.gz *
echo "Backup creado"