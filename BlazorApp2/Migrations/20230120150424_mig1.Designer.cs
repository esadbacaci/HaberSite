﻿// <auto-generated />
using BlazorApp2.Context;
using Microsoft.EntityFrameworkCore;
using Microsoft.EntityFrameworkCore.Infrastructure;
using Microsoft.EntityFrameworkCore.Metadata;
using Microsoft.EntityFrameworkCore.Migrations;
using Microsoft.EntityFrameworkCore.Storage.ValueConversion;

namespace BlazorApp2.Migrations
{
    [DbContext(typeof(HaberDbContext))]
    [Migration("20230120150424_mig1")]
    partial class mig1
    {
        protected override void BuildTargetModel(ModelBuilder modelBuilder)
        {
#pragma warning disable 612, 618
            modelBuilder
                .HasAnnotation("ProductVersion", "3.1.1")
                .HasAnnotation("Relational:MaxIdentifierLength", 128)
                .HasAnnotation("SqlServer:ValueGenerationStrategy", SqlServerValueGenerationStrategy.IdentityColumn);

            modelBuilder.Entity("BlazorApp2.Models.Haber", b =>
                {
                    b.Property<int>("HaberId")
                        .ValueGeneratedOnAdd()
                        .HasColumnType("int")
                        .HasAnnotation("SqlServer:ValueGenerationStrategy", SqlServerValueGenerationStrategy.IdentityColumn);

                    b.Property<string>("HaberAuthor")
                        .HasColumnType("nvarchar(max)");

                    b.Property<string>("HaberCategory")
                        .HasColumnType("nvarchar(max)");

                    b.Property<string>("HaberDescription")
                        .HasColumnType("nvarchar(max)");

                    b.Property<string>("HaberImage")
                        .HasColumnType("nvarchar(max)");

                    b.Property<string>("HaberTitle")
                        .HasColumnType("nvarchar(max)");

                    b.HasKey("HaberId");

                    b.ToTable("habers");
                });
#pragma warning restore 612, 618
        }
    }
}
