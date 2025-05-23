#!/bin/bash
echo "🔨 Fazendo build da aplicação DimDim..."
docker build -t dimdim-app .
echo "✅ Build concluído!"
